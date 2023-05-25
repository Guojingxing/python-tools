import re
from bs4 import BeautifulSoup

# 读取本地HTML文件
with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 查找所有a标签
a_tags = soup.find_all('a')

# 提取符合要求的a标签的href和title属性
youtube_links = []
for a_tag in a_tags:
    href = a_tag.get('href')
    title = a_tag.get('title')
    if href and title:
        # 使用正则表达式提取视频ID
        match = re.search(r'/watch\?v=([a-zA-Z0-9_\-]+)', href)
        if match:
            video_id = match.group(1)
            youtube_link = f'<youtube>{video_id}</youtube>'
            youtube_links.append((title, youtube_link))

# 将提取到的标题和链接写入output.txt文件
with open('output_formatted.txt', 'w', encoding='utf-8') as output_file:
    for title, link in youtube_links:
        output_file.write(f'{title}\n{link}\n')

print('提取完成，结果已写入output_formatted.txt文件。')
