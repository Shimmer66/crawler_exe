import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()


def main():
    url_base = 'http://ssr1.scrape.center/page/'
    movie_info_all = []

    for i in range(1, 11):
        url = url_base + str(i)
        soup = get_res(url)

        for cla in soup.find_all('div', class_='el-card item m-t is-hover-shadow'):
            movie_info = {}

            # 提取图片链接
            image_src = [img['src'] for img in cla.find_all('img', class_='cover')]
            movie_info['image_src'] = image_src[0] if image_src else None

            # 提取电影名称
            movie_name = [h2.text for h2 in cla.find_all('h2', class_='m-b-sm')]
            movie_info['movie_name'] = movie_name[0] if movie_name else None

            # 提取电影分类和地区
            categories = [button.text.strip('\n') for button in cla.find_all('button')]
            regions = [span.text.replace('/', '') for info in cla.find_all('div', class_='m-v-sm info')
                       for span in info.find_all('span')]
            movie_info['categories'] = ' '.join(categories)
            movie_info['region'] = ''.join(regions)

            # 提取评分
            rating = [p.text.strip() for p in cla.find_all('p', class_='score')]
            movie_info['rating'] = rating[0] if rating else None

            movie_info_all.append(movie_info)

    # 打印提取的数据
    for index, movie_info in enumerate(movie_info_all, start=1):
        print(f'Movie {index}:')
        print('Image Source:', movie_info['image_src'])
        print('Movie Name:', movie_info['movie_name'])
        print('Categories:', movie_info['categories'])
        print('Region:', movie_info['region'])
        print('Rating:', movie_info['rating'])


def get_res(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q'
    }
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


if __name__ == '__main__':
    main()
