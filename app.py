import requests
from bs4 import BeautifulSoup
import csv
import time
import json

class WebScraper:
    def __init__(self, config_file, page_sleep=2):
        filename = config_file.split('/')[-1]
        filename = filename.split('.')[0]

        self.output_dir = 'output/' + filename + '.csv'
        self.config = self.read_json(config_file)
        self.crawled_data = []
        self.visite_links = []
        self.visited_links = []

        # ページのスリープ時間
        self.page_sleep = page_sleep

        # CSVファイルの初期化
        self.init_csv()

    # データ抽出関数
    def extract_data(self, soup, selector, attr=None):
        elements = soup.select(selector)
        if attr:
            return [element.get(attr) for element in elements if element.get(attr)]
        else:
            return [element.text.strip() for element in elements if element.text.strip()]

    # クロール関数
    def crawl_web(self):
        start_url = self.config['startUrl'][0]
        
        # 開始URLのコンテンツを取得
        response = requests.get(start_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # リンクの抽出
        link_selector = next(item for item in self.config['selectors'] if item['id'] == 'links')['selector']
        links = self.extract_data(soup, link_selector, 'href')
        self.visite_links.extend(links)

        # 各リンクの処理
        while self.visite_links:
            # if link.startswith('/'):
            #     link = start_url + link
            link = self.visite_links.pop(0)
            print(f"Processing link: {link}(all: {len(self.visite_links)})")

            link_response = requests.get(link)
            link_soup = BeautifulSoup(link_response.content, 'html.parser')
            
            # ページネーションリンクの抽出
            pagenation_selector = next(item for item in self.config['selectors'] if item['id'] == 'pagenation')['selector']
            pagelinks = self.extract_data(link_soup, pagenation_selector, 'href')
            for pagelink in pagelinks:
                self.add_link(pagelink)

            # ドメイン情報の抽出
            domain_selector = next(item for item in self.config['selectors'] if item['id'] == 'domain')['selector']
            domains = self.extract_data(link_soup, domain_selector)

            # 抽出した情報の保存
            for domain in domains:
                self.crawled_data.append([domain])
            
            self.visited_links.append(link)
            time.sleep(self.page_sleep)

    def add_link(self, link):
        if link not in self.visite_links and link not in self.visited_links:
            # add link to the front of the self.visite_links
            self.visite_links.insert(0, link)

    def read_json(self, json_file):
        with open(json_file, 'r') as file:
            config = json.load(file)
        return config
    
    def init_csv(self):
        with open(self.output_dir, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["domain"])

    def save_csv(self):
        with open(self.output_dir, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["domain"]) # "start_url", "link"
            writer.writerows(self.crawled_data)

        print(f"データが '{self.output_dir}' に保存されました。")

if __name__ == "__main__":
    try:
     
        json_file = "input/website1.json"
        page_sleep = 2

        crawler = WebScraper(json_file, page_sleep)
        crawler.crawl_web()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # データをCSVに保存
        crawler.save_csv()
        print("処理が完了しました。")
