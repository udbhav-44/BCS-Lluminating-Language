import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class IITKArticlesScraper(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        super(IITKArticlesScraper, self).__init__(*args, **kwargs)
        self.implicitly_wait(10)

    def open_page_5(self):
        self.get(f"https://voxiitk.com/category/all-about-iitk/page/5/")
        self.maximize_window()
    def open_page_6(self):
        self.get(f"https://voxiitk.com/category/all-about-iitk/page/6/")
        self.maximize_window()

    def scrape_articles(self):
        articles_data = []
        article_elements = self.find_elements(By.XPATH, '//article')
        length = len(article_elements)
        
        for i in range(length):
            time.sleep(2)
            article_elements = self.find_elements(By.XPATH, '//article')
            article = article_elements[i]
            title_element = article.find_element(By.XPATH, './/h2[@class="heading-title-text"]//a')
            print(title_element.get_attribute('href'))
            title = title_element.text.strip()
            link = title_element.get_attribute('href')
            date = article.find_element(By.XPATH, './/time[@class="entry-date published"]').text.strip()
            
            try:
                summary = article.find_element(By.XPATH, './/div[@class="post-excerpt"]').text.strip()
            except NoSuchElementException:
                summary = "Summary not available"
            
            self.get(link)
            content = self.find_element(By.CLASS_NAME, 'svq-site-content').text.strip()
            articles_data.append([title, date, summary, content, link])
            self.back()
            time.sleep(2)
        
        return articles_data

    def save_to_text_file(self, articles_data):
        with open('IITK_Articles_scraped_vox_Rounak2.txt', 'w', encoding='utf-8') as f:
            for article in articles_data:
                f.write(f"Title: {article[0]}\n")
                f.write(f"Date: {article[1]}\n")
                f.write(f"Summary: {article[2]}\n")
                f.write(f"Content: {article[3]}\n")
                f.write(f"Link: {article[4]}\n")
                f.write("\n" + "="*80 + "\n\n")
        print("Data saved to IITK_Articles_scraped_vox_Rounak2.txt")

if __name__ == "__main__":
    bot = IITKArticlesScraper()

    bot.open_page_5()
    articles = bot.scrape_articles()
    bot.save_to_text_file(articles)
    bot.open_page_6()
    articles = bot.scrape_articles()
    bot.save_to_text_file(articles)

    bot.quit()
