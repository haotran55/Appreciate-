from telethon import TelegramClient, events
import asyncio

# Thay API ID và HASH của bạn
api_id = 28994972  # Không dùng dấu nháy
api_hash = 'f67f3f73fa5bbeff5b58467fb9c12ffb'

# Nội dung trả lời tự động
response_message = (
    "Xin chào, đây là bot tự động trả lời. Hiện tại chủ tài khoản đã offline. "
    "Vui lòng liên hệ qua Zalo hoặc Facebook. Xin cảm ơn! "
    "(Đây chỉ là bot trả lời tự động do chủ tài khoản tạo ra, "
    "nên không có quyền trò chuyện như con người). Xin cảm ơn!"
)

client = TelegramClient('user_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private and not event.out:  # Chỉ trả lời tin nhắn riêng, không phải tin mình gửi
        await event.respond(response_message)

async def main():
    await client.start()
    print(">> Bot đang chạy... Nhấn Ctrl+C để dừng.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
