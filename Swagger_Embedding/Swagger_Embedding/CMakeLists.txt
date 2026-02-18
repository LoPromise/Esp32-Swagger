# Execute the python script before building the binary
add_custom_command(
    OUTPUT "${CMAKE_CURRENT_SOURCE_DIR}/web/index.html.gz"
    COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/generate_swagger.py
    DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/openapi.yaml"
    VERBATIM
)

# Register the component and embed the generated file
idf_component_register(INCLUDE "gen/generated_api.h"
                       EMBED_FILES "web/index.html.gz")