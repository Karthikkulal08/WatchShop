from django.contrib import admin
from .models import Watches, WatchesUpload, Wishlist, Cart

# Register Watches model
admin.site.register(Watches)

# Define the admin interface for WatchesUpload
class WatchesUploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    list_filter = ('name', 'price')
    search_fields = ('name', 'description')
    fields = ['name', 'price', 'description', 'image']

# Register WatchesUpload model with custom admin interface
admin.site.register(WatchesUpload, WatchesUploadAdmin)

# Register Wishlist model
admin.site.register(Wishlist)

# Register Cart model (if defined)
admin.site.register(Cart)
