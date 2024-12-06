# admin.py (contributionApp)
from django.contrib import admin
from accounts.models import User
from .models import Point

# admin.site.register(User)
# @admin.register(User)
admin.site.register(User)

#追加した
from .models import Item
admin.site.register(Item)


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    # 一覧表示のフィールドを指定
    list_display = ('user', 'activity_name', 'points_requested', 'date', 'is_approved', 'created_at')
    
    # フィルタ機能を追加
    list_filter = ('is_approved', 'date')
    
    # 検索機能を追加
    search_fields = ('activity_name', 'user__username')
    
    # 一括操作を有効化
    actions = ['approve_contributions', 'reject_contributions']

    # 一括承認のアクション
    @admin.action(description="選択した申請を承認する")
    def approve_contributions(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()}件の申請を承認しました。")

    # 一括却下のアクション
    @admin.action(description="選択した申請を却下する")
    def reject_contributions(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"{queryset.count()}件の申請を却下しました。")
