app_name = "library_management_system"
app_title = "Library Management System"
app_publisher = "muletasisay"
app_description = "LMS challenge at 360 Ground"
app_email = "muletasi12@gmail.com"
app_license = "mit"

# REST API endpoints

# Define the API routes
override_whitelisted_methods = {
    "POST": {

        # book related
        "create_book": "library_management_system.library_management_system.api.create_book",
        "get_book": "library_management_system.library_management_system.api.get_book",
        "get_books": "library_management_system.library_management_system.api.get_books",
        "update_book": "library_management_system.library_management_system.api.update_book",
        "delete_book": "library_management_system.library_management_system.api.delete_book",
        
        # member releated
        "create_member": "library_management_system.library_management_system.api.create_member",
        "get_member": "library_management_system.library_management_system.api.get_member",
        "get_members": "library_management_system.library_management_system.api.get_members",
        "update_member": "library_management_system.library_management_system.api.update_member",
        "delete_member": "library_management_system.library_management_system.api.delete_member"
    # 
    }
}

# permission role
permission_query_conditions = {
    "Book": "library_management_system.library_management_system.permissions.get_permission_query",
    "Member": "library_management_system.library_management_system.permissions.get_permission_query"

}
