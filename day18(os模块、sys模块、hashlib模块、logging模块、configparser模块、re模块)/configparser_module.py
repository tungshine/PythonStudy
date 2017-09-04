# __author: TungShine
# __date: 2017/9/4
# __descritption: 用于生成和修改配置文件

import configparser

config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)

print(config.sections())
config.read('config.ini')
print(config.sections())
print('bytebong.com' in config)# False
print(config['bitbucket.org']['User'])
