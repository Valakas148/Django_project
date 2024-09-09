# from djangochannelsrestframework.decorators import action
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.observer import model_observer
#
# from apps.announcement.models import Announcement
# from apps.announcement.serializer import AnnouncementSerializer
#
#
# class AnnouncementConsumer(GenericAsyncAPIConsumer):
#     def __init__(self, *args, **kwargs):
#         self.room_name = 'cars'
#         super().__init__(*args, **kwargs)
#
#     async def connect(self):
#         if not self.scope['user']:
#             return await self.close()
#         await self.accept()
#         await self.channel_layer.group_add(
#             self.room_name,
#             self.channel_name,
#         )
#
#     @model_observer(Announcement,serializer_class=AnnouncementSerializer)
#     async def announcement_activity(self, message, action, subscribing_request_id, **kwargs):
#         for request_id in subscribing_request_id:
#             await self.reply(data=message, action=action, request_id=request_id)
#
#     @action()
#     async def subscribe_to_announcement_activity(self, request_id, **kwargs):
#         await self.announcement_activity.subscribe(request_id=request_id)