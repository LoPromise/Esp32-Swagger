Purpose of this project is to provide an example how to do in Situ dokumentation for an ESP32 REST API using industry standard Tooling Swagger(Openapi), autogenerating the API Server so only callbacks are needed to embed it into Production code. Ensuring that Documentation and Implementation is consistant.

Oviously in an actual application you wouldnt just set outputs you got a whole core sitting there hungrily waiting for your embedded code.

Why this works most modern browsers accept zipped content which we use here to provide the page from the ESP. This leaves us with less Overall Size.

Why do this:    Open documentation on the device itself cant get lost no furter hosting required, no lost manual.
                Automation of Implementation for every entry in the yaml a callback is created automatically you just have to hock your code to it.

Cons:           The Embedded HTML Page may be bigger than the actual yaml, but this is outweigth by just having the manual in the browser.
                would putting it on the controller as a text file work just as well: yes. this is aimed at the diy crowd or less low level devs, that are likely the customers you would do something like this for.

Requirements: Cmake
              ESP-IDF
              python