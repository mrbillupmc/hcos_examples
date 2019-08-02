README file for Simple hcOS Swagger Client Example

This README describes how to augment a simple Java project using the hcOS API generated from its Swagger YAML file.  The intent is to demonstrate how easy it is to add hcOS support to an existing project.

# Create a New Maven Project
For purposes of this document we will assume that a Maven project already exists with a pom.xml file and corresponding file structure.  We want to add command line support to the project to make it easier to share:

```
$ mvn -N io.takari:maven:0.7.6:wrapper
```

You may want to add a simple class and unit test to make sure everything is working properly.

```
$ ./mvnw clean package
...
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  3.317 s
[INFO] Finished at: 2019-07-09T11:07:05-04:00
[INFO] ------------------------------------------------------------------------
```

# Generate API Classes from Swagger YAML
Locate the version of the hcOS API Swagger YAML file that you wish to use and place it in the __hcos-api__ subdirectory.

```
$ mkdir hcos-api
$ cd hcos-api
$ cp /path/to/swagger.yaml swagger.yaml
```

At this point you could download, install (e.g., brew install swagger-codegen on a Mac) and use the swagger-codegen package to generate the code - for example:

```
$ swagger-codegen generate -i swagger.yaml \
-l java --api-package com.upmc.enterprises.hcos.api \
--model-package com.upmc.enterprises.hcos.model \
-o swagger-generated-code
```

OR

## Create a Maven Build
The pom.xml used to generate the classes acts as an historical artifact of how it was done.  First, we make a pom.xml:

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.upmc.enterprises</groupId>
    <artifactId>hcos-api-generation</artifactId>
    <packaging>jar</packaging>
    <version>1.0</version>
    <name>hcos-api-generation-project</name>
    <url>https://github.com/upmc-enterprises/hcos_examples</url>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    <build>
        <plugins>
            <!-- activate the plugin -->
            <plugin>
                <groupId>io.swagger.codegen.v3</groupId>
                <artifactId>swagger-codegen-maven-plugin</artifactId>
                <version>3.0.8</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>generate</goal>
                        </goals>
                        <configuration>
                            <!-- specify the swagger yaml -->
                            <inputSpec>${project.basedir}/swagger.yaml</inputSpec>
                            <output>${project.basedir}/hcos-api-generated</output>

                            <!-- target to generate java client code -->
                            <language>java</language>

                            <!-- pass any necessary config options -->
                            <configOptions>
                                <apiPackage>com.upmc.enterprises.hcos.api</apiPackage>
                                <modelPackage>com.upmc.enterprises.hcos.model</modelPackage>
                            </configOptions>


                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    <dependencies>
        <!-- https://mvnrepository.com/artifact/com.squareup.okhttp/okhttp -->
        <dependency>
            <groupId>com.squareup.okhttp</groupId>
            <artifactId>okhttp</artifactId>
            <version>2.7.5</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.squareup.okhttp/logging-interceptor -->
        <dependency>
            <groupId>com.squareup.okhttp</groupId>
            <artifactId>logging-interceptor</artifactId>
            <version>2.7.5</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/com.google.code.gson/gson -->
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.8.1</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.threeten/threetenbp -->
        <dependency>
            <groupId>org.threeten</groupId>
            <artifactId>threetenbp</artifactId>
            <version>1.3.5</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/io.swagger.core.v3/swagger-annotations -->
        <dependency>
            <groupId>io.swagger.core.v3</groupId>
            <artifactId>swagger-annotations</artifactId>
            <version>2.0.0</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/io.gsonfire/gson-fire -->
        <dependency>
            <groupId>io.gsonfire</groupId>
            <artifactId>gson-fire</artifactId>
            <version>1.8.3</version>
        </dependency>

    </dependencies>

</project>
```


Then, we do the Maven build.  

```
$ cd hcos-api
$ ../mvnw clean compile
```
At this point the Java source for the hcOS API has been generated in the __hcos-api-generated__ subdirectory.  At this point there are three options for making it available to your application.
<ol>
<li>Copy the source files and add them to your project's source.</li>
<li>Generate the jar file and add it to your own Maven repository.</li>
<li>Generate the jar file and add it to a local (to the project) Maven repository.</li>
</ol>

For the purposes of our exercise we will choose to build the jar and add it to a Maven repository that is local to the project.

```
$ cd hcos-api-generated
$ ../../mvnw clean package
$ cd ../..
$ mkdir -p hcos-api-repo
$ ./mvnw install:install-file -Dfile=./hcos-api/hcos-api-generated/target/swagger-java-client-1.0.0.jar -DgroupId=com.upmc.enterprises.hcos -DartifactId=swagger-java-client -Dversion=1.0 -Dpackaging=jar -DlocalRepositoryPath=hcos-api-repo
```

Now the point has been reached where the hcOS API jar and its dependencies may be added to the target Maven project.

# Add It To Your Project
The hcOS API jar dependency can be added to the target project in this way.
## Tell Maven About the Local Repository
The target project needs to have the pom.xml file modified to let it know where the local repository resides.

```
<repositories>
        <repository>
            <id>hcos-api-repo</id>
            <url>file://${basedir}/hcos-api-repo</url>
        </repository>
</repositories>
```
## Add the Dependency for the hcOS API
Modify the POM for the jr dependency in the local repository.

```
        <dependency>
            <groupId>com.upmc.enterprises.hcos</groupId>
            <artifactId>swagger-java-client</artifactId>
            <version>1.0</version>
        </dependency>
```

## Add the Other Required Dependencies.
The Swagger code generator requires the following dependencies for the API jar that was created.
<ul>
<li>okhttp:2.7.5</li>
<li>logging-interceptor:2.7.5</li>
<li>gson:2.8.1</li>
<li>threetenbp:1.3.5</li>
<li>gson-fire:1.8.3</li>
 </ul>

There are other libraries supported by the Swagger generator that could be used to communicate with the hcOS API server, but the default one seems to have the fewest additional dependencies.  The following command will give an idea of the available options:

```
$ swagger-codegen config-help -l java
```

# Use It!
At this point the API classes should be able to be referenced in the target project.  See __GettingStarted__ and __GettingStartedTest__ for straightforward examples of usage.  If you have a proper ```Configuration.json``` file you should be able to run the example from the command line.

```
$ ./mvnw clean test
```




