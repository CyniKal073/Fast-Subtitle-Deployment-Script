import os

'''
注意：字幕文件须直接保存在名为“Subs”的文件夹目录下，且每集仅限一个字幕。
'''
sub_names = os.listdir('subs')
video_names = os.listdir()
i = 0
for video_name in video_names:
    if (video_name[-3:] == 'ass'):
        os.remove(video_name)
    if (video_name[-3:] == 'mkv'):
        sub = open('%s.ass' %(video_name[:-4]), 'wb')
        ass = open('Subs/%s' %(sub_names[i]), 'rb')
        content = ass.read()
        sub.write(content)
        i = i + 1
        sub.close()
        ass.close()

