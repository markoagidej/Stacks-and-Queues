# Task 1: Design a Stack-based structure to represent your browsing history where you have the ability to:  
'''Add a new page (add to the Stack)
Remove a page (Remove from the Stack)
Check to see how many pages you have viewed in your browsing session
Check to see if you current browsing session is empty.'''

class BrowserHistoryStack:
    def __init__(self):
        self.history = []
    
    def add_page(self, pageURL):
        self.history.append(pageURL)

    def remove_page(self):
        if self.history != []:
            return self.history.pop()
        
    def count_pages(self):
        return len(self.history)
        
    def check_history_exists(self):
        return self.history != []
    
browser = BrowserHistoryStack()
browser.add_page("google")
browser.add_page("facebook")
browser.add_page("instagram")
print(f"{browser.count_pages()} pages in history")
print(f"History?: {browser.check_history_exists()}")
print(browser.remove_page())
print(f"{browser.count_pages()} pages in history")
print(browser.remove_page())
print(browser.remove_page())
print(browser.remove_page())
print(f"{browser.count_pages()} pages in history")
print(f"History?: {browser.check_history_exists()}")