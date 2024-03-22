from winotify import Notification, audio

toast = Notification(app_id="Message", title="Message Title", msg="Hello world!", duration="long",
                     icon=r"C:\Users\user\Desktop\GORKEM\python_development\notifiy_message_icon.png")
toast.set_audio(audio.Default, loop=False)
toast.add_actions(label="Click me!", launch="https://github.com/yusufgorkem")
toast.show()
