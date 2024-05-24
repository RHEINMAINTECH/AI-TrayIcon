import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

class SystemTrayApp:
    def __init__(self, url1, url2, url3, url4):
        self.url1 = url1
        self.url2 = url2
        self.url3 = url3
        self.url4 = url4
        self.app = QApplication(sys.argv)

        # Set up the system tray
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self.app)
        self.tray_menu = QMenu()

        self.open_url1_action = QAction("Open ChatGPT 3.5")
        self.open_url2_action = QAction("Open ChatGPT 4o")
        self.open_url3_action = QAction("Open ChatGPT 4")
        self.open_url4_action = QAction("Open HF-Chat")
        self.exit_action = QAction("Exit")

        self.tray_menu.addAction(self.open_url1_action)
        self.tray_menu.addAction(self.open_url2_action)
        self.tray_menu.addAction(self.open_url3_action)
        self.tray_menu.addAction(self.open_url4_action)
        self.tray_menu.addAction(self.exit_action)

        self.tray_icon.setContextMenu(self.tray_menu)

        # Connect actions
        self.open_url1_action.triggered.connect(lambda: self.open_browser(self.url1))
        self.open_url2_action.triggered.connect(lambda: self.open_browser(self.url2))
        self.open_url3_action.triggered.connect(lambda: self.open_browser(self.url3))
        self.open_url4_action.triggered.connect(lambda: self.open_browser(self.url4))
        self.exit_action.triggered.connect(self.exit_app)

        # Show the system tray icon
        self.tray_icon.show()

    def open_browser(self, url):
        # Provide the full path to the Chrome executable
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # Update this path if needed

        # Verify if the path exists
        if not subprocess.os.path.exists(chrome_path):
            print(f"Chrome executable not found at {chrome_path}. Please check the path.")
            return

        # Command to open Chrome in kiosk mode without toolbar and window frame
        chrome_command = [
            chrome_path,
            "--app={}".format(url),
            "--window-position=1200,900",  # Adjust this according to your screen resolution
            "--window-size=750,600"  # Adjust this according to the desired window size
        ]
        try:
            subprocess.Popen(chrome_command)
        except Exception as e:
            print(f"Failed to open Chrome: {e}")

    def exit_app(self):
        self.tray_icon.hide()
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    url1 = "https://chatgpt.com/?model=text-davinci-002-render-sha"  # ChatGPT 3.5
    url2 = "https://chatgpt.com/?model=gpt-4o"  # ChatGPT 4o
    url3 = "https://chatgpt.com/?model=gpt-4"  # ChatGPT 4
    url4 = "https://huggingface.co/chat"  # HF-Chat
    app = SystemTrayApp(url1, url2, url3, url4)
    app.run()
