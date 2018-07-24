
# Author:ph
class HtmlOutputer():
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return None
        self.datas.append(data)


    def output_html(self):
        fileout = open('output.html','w')
        fileout.write("<html>")
        fileout.write("<body>")
        fileout.write("<table>")
        #ascii
        for data in self.datas:
            fileout.write("<tr>")
            fileout.write("<td>%s</td>" % data['url'])
            fileout.write("<td>%s</td>" % data['title']).encode('utf-8')
            fileout.write("<td>%s</td>" % data['summary']).encode('utf-8')
            fileout.write("</tr>")
        fileout.write("</table>")
        fileout.write("</body>")
        fileout.write("</html>")
