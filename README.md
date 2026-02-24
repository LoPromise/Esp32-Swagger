# ESP32 REST API Documentation with Swagger/OpenAPI

## Overview
This project demonstrates how to implement in-situ documentation for an ESP32 REST API using industry-standard tooling (Swagger/OpenAPI). It automatically generates the API server, requiring only callbacks to embed into production code. This ensures consistency between documentation and implementation.

> **Note**: In a real application, you'd have a full core system, not just output setting.

---

## Why This Works

Modern browsers support zipped content, which we leverage to serve the documentation page directly from the ESP. This approach:

- **Eliminates external hosting** requirements – documentation is self-contained on the device.
- **Automates implementation**: Every entry in the YAML file generates a callback. You only need to hook your code to these callbacks.
- **Shifts development effort**: Reduces the burden on embedded developers, allowing focus on actual algorithm and enhanching time to product.

---

## Considerations
### Todos:
- **Settings**:  
- ***Generate just header and not embed the file***
- ***proper idf component***
- ***extracting response codes and autogenerate code from there***
### Benefits
- **Self-contained documentation**: No risk of lost manuals or hosting dependencies.
- **Efficiency**: Automation reduces manual API implementation effort.

### Trade-offs
- **File size**: The embedded HTML page may be larger than the YAML file. However, this is offset by having the manual directly accessible in the browser.
- **Alternative approaches**: Storing documentation as a text file on the controller would work similarly, but this method targets DIY enthusiasts or less low-level developers.

---

## Requirements

To use this project, ensure you have the following tools installed:

- [CMake](https://cmake.org/)
- [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/)
- [Python](https://www.python.org/)

---

## Getting Started

1. Clone the repository: `git clone https://github.com/LoPromise/Esp32-Swagger.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Build the project using CMake and ESP-IDF.