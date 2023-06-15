#buttons do not function: reload, back, forward, home etc
#added a search button. when using in browser it closes program

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5.QtWebEngineWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Set the initial URL to Google.
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.browser.urlChanged.connect(self.update_urlbar)# Connect the URl changed signal to the update_urlbar
        self.browser.loadFinished.connect(self.update_title)# Connect the load finished signal to the update_title() method.
        self.setCentralWidget(self.browser)# Set the browser as the central widget.
        self.browser = QWebEngineView()
        # Create a status bar.
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # Create a toolbar.
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        # Back button
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)


        # Forward button
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to the next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # Home button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go Home")
        home_btn.triggered.connect(self.navigation_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()
        # Create a URL bar.
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        # Search button
        search_btn = QAction("Search", self)
        search_btn.setStatusTip("Search up")
        search_btn.triggered.connect(self.browser.load)
        navtb.addAction(search_btn)

        # Stop button
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.show()

#title
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Nate's Browser" % title)
#home url
    def navigation_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))
#scheme: http
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(QUrl(self.urlbar.text()))
        self.browser.setUrl(q)
#url bar
    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.browser.setUrl(QUrl(self.urlbar.text()))
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)
app.setApplicationName("Nate's Browser")
window = MainWindow()
sys.exit(app.exec_())
