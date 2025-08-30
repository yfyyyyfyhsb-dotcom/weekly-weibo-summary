from pathlib import Path

bloggers = {
  "5172202845": "这一周主要分享了日常生活和个人感悟，偶尔配上温柔文字。",
  "6329703990": "分享了音乐和旅行的点滴，感受生活的细腻和温度。",
  "1849722175": "更多是自我心情记录，有感而发，充满小小感慨。",
  "7893326676": "分享生活灵感和创作点子，让人有轻轻温暖感。",
  "7132673657": "记录日常和内心感受，字里行间带着柔软感。"
}

html = "<html>\n<head>\n<meta charset='UTF-8'>\n<title>本周微博总结</title>\n</head>\n<body>\n"
html += "<h1>📖 本周微博总结</h1>\n"

for id, summary in bloggers.items():
  html += f"<div>\n<h2>博主 {id}</h2>\n<p>{summary}</p>\n</div>\n"
  html += "</body>\n</html>" Path("weekly_summary.html").write_text(html, encoding="utf-8")
