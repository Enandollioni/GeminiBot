from telebot import types
import google.generativeai as genai
import logging
import PIL.Image
import io
# эта функция создаст все обработчики и зарегистрирует их в предоставленном боте


def register_handlers(bot, convo):

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        max_len = 4096
        if message.content_type == 'text':
            convo.send_message(message.text)
            response_text = convo.last.text
            if len(response_text) > max_len:
                for x in range(0, len(response_text), max_len):
                    part = response_text[x: x + max_len]  # Split the response into parts
                    bot.reply_to(message, part)
            else:
                bot.reply_to(message, response_text)
        elif message.content_type == 'photo':
            convo.send_photo(message.photo)
            response1 = convo.last.image
            bot.reply_to(message, response1)

    # @bot.message_handler(commands=['gemi'])
    # async def gemi_handler(message: types.Message):
    #     loading_message = None  # Initialize loading_message outside the try block
    #     try:
    #         # Display a loading message
    #         loading_message = await message.answer("<b>Generating response, please wait...</b>", parse_mode='html')
    #
    #         # Check if there's a prompt or not
    #         if len(message.text.strip()) <= 5:
    #             await message.answer("<b>Please provide a prompt after the command.</b>", parse_mode='html')
    #             return
    #
    #         # Get the text following the /gemi command as the prompt
    #         # prompt = message.text.split(maxsplit=1)[1:] # данный участок кода пока на перестройке
    #         # response = model.generate_content(prompt) # данный участок кода пока на перестройке
    #         # response_text = response.text # данный участок кода пока на перестройке
    #         response_text = convo.last.text # моя догадка как сделать, чтобы работало
    #
    #         # Split the response if it's over 4000 characters
    #         if len(response_text) > 4000:
    #             # Split the response into parts
    #             parts = [response_text[i:i+4000] for i in range(0, len(response_text), 4000)]
    #             for part in parts:
    #                 await message.answer(part, parse_mode='markdown')
    #         else:
    #             # Send the response as a single message
    #             await message.answer(response_text, parse_mode='markdown')
    #
    #     except Exception as e:
    #         await message.answer(f"An error occurred: {str(e)}")
    #     finally:
    #         # Delete the loading message regardless of whether an error occurred or not
    #         if loading_message:
    #             await bot.delete_message(chat_id=loading_message.chat.id, message_id=loading_message.message_id)
   # @bot.message_handler(commands=['imgai'])
    # async def generate_from_image(message: types.Message):
    #     if convo.reply_to(message) and convo.reply_to(message.photo):
    #         image = convo.reply_to(message.photo[-1])
    #         prompt = message.get_args() or convo.reply_to(message.caption) or "Describe this image."
    #         processing_message = await message.answer("<b>Generating response, please wait...</b>", parse_mode='html')
    #
    #         try:
    #             # Fetch image from Telegram
    #             img_data = await bot.download_file_by_id(image.file_id)
    #             img = PIL.Image.open(io.BytesIO(img_data.getvalue()))
    #
    #             # Generate content
    #             response = model.generate_content([prompt, img])
    #             response_text = response.text
    #
    #             # Send the response as plain text
    #             await message.answer(response_text, parse_mode=None)
    #         except Exception as e:
    #             await message.answer("<b>An error occurred. Please try again.</b>", parse_mode='html')
    #         finally:
    #             await bot.delete_message(chat_id=processing_message.chat.id, message_id=processing_message.message_id)
    #     else:
    #         await message.answer("<b>Please reply to an image with this command.</b>", parse_mode='html')


if __name__ == '__main__':
    print('Этот код выполнится ТОЛЬКО если файл запущен напрямую.')
    print('Он не выполнится при импорте файла.')
