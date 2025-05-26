from django.contrib import admin
from .models import (
    Project, Tag, ProjectPicture, Donation,
    Comment, ProjectReport, CommentReport, ProjectRating
)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'category', 'total_target', 'start_time', 'end_time', 'is_featured', 'is_canceled')
    search_fields = ('title', 'creator__username')
    list_filter = ('is_featured', 'is_canceled', 'category')
    date_hierarchy = 'start_time'
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ProjectPicture)
class ProjectPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'image')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'amount', 'donated_at')
    search_fields = ('user__username', 'project__title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'content', 'created_at', 'parent')
    search_fields = ('user__username', 'project__title', 'content')

@admin.register(ProjectReport)
class ProjectReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'reason', 'created_at')

@admin.register(CommentReport)
class CommentReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'reason', 'created_at')

@admin.register(ProjectRating)
class ProjectRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'rating', 'created_at')
