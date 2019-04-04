from urllib import request
from io import  BytesIO
import  gzip
import re

class Spider():

	url = 'https://www.douyu.com/g_DOTA2'
	rootPattern = '<li class="layout-Cover-item">([\s\S]*?)</li>'
	herf_pattern = 'href="([\s\S]*?)"'
	room_pattern = 'title="([\s\S]*?)"'
	name_pattern = '<h2 class="DyListCover-user">([\s\S]*?)</h2>'

	def __fetch_content(self):
		# r = request.urlopen(Spider.url)
		# htmls = str(r.read(), encoding='utf-8')
		# print(htmls)
		# print(r)
		req = request.Request(Spider.url)
		req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
		req.add_header("Accept-Encoding", "gzip, deflate, br")
		req.add_header("referer", "https://www.douyu.com/")
		# req.add_header(":authority", "www.zhihu.com")
		print(dict(req.headers))

		r = request.urlopen(req).read()
		buff = BytesIO(r)
		f = gzip.GzipFile(fileobj=buff)

		html = f.read().decode('utf-8')

		# print(html)

		return html


	def __analysis(self, htmls):
		item_list = re.findall(Spider.rootPattern, htmls)
		info_list = []

		l = lambda html: {
			'herf': re.findall(Spider.herf_pattern, html)[0].strip(),
			'room': re.findall(Spider.room_pattern, html)[0].strip(),
			'name': re.findall(Spider.name_pattern, html)[0].strip()
		}

		info_list = map(l, item_list)

		# for html in item_list:
		# 	herf = re.findall(Spider.herf_pattern, html)
		# 	room = re.findall(Spider.room_pattern, html)
		# 	name = re.findall(Spider.name_pattern, html)
		#
		# 	temp_info = {'herf': herf, 'room': room, 'name': name}
		#
		# 	info_list.append(temp_info)

		print(list(info_list))

	# 精炼数据
	def __refine(self, info_lists):
		pass

		l = lambda info_list: {}

	def get_content(self):
		return self.__fetch_content()

	def get_partten_list(self, htmls):
		self.__analysis(htmls=htmls)


a = Spider()
htmls = a.get_content()

a.get_partten_list(htmls)