from django.contrib import admin

from project.feed.models import Restaurant, Review, Comment, Profile, Category, ReviewLike, CommentLike


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'country', 'street', 'city', 'zip', 'website', 'phone_number',
                    'email', 'opening_hours', 'price_level', 'image']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'restaurant', 'content', 'rating']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'content']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'phone_number', 'things_love', 'description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'review']


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewLike, ReviewLikeAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
