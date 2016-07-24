# -*- coding: utf-8 -*-
"""
Created on Wed May 28 01:22:20 2014

@author: Vespa
"""

class User():
    def __init__(self,m_mid=None,m_name=None):
        if m_mid:
            self.mid = m_mid
        if m_name:
            if isinstance(m_name,unicode):
                m_name = m_name.encode('utf8')
            self.name = m_name
#   获取空间地址
    def GetSpace(self):
        return 'http://space.bilibili.tv/'+str(self.mid)
    mid = None
    name = None
    isApprove = None#是否是认证账号
    spaceName = None
    sex = None
    rank = None
    avatar = None
    follow = None#关注好友数目
    fans = None#粉丝数目
    article = None#投稿数
    place = None#所在地
    description = None#认证用户为认证信息 普通用户为交友宣言
    followlist = None#关注的好友列表
    friend = None
    DisplayRank = None
    message = None # 承包时会返回的承保信息


class Video():
    def __init__(self,m_aid=None,m_title=None):
        if m_aid:
            self.aid = m_aid
        if m_title:
            if isinstance(m_title,unicode):
                m_title = m_title.encode('utf8')
            self.title = m_title
    aid = None
    title = None
    guankan = None
    shoucang = None
    danmu = None
    date = None
    cover = None
    commentNumber = None
    description = None
    tag = None
    author = None
    page = None
    credit = None
    coin = None
    spid = None
    cid = None
    offsite = None#Flash播放调用地址
    Iscopy = None
    subtitle = None
    duration = None
    episode = None
    arcurl = None#网页地址
    arcrank = None#不明
    tid = None
    index = None#剧番中的集数
    episode_id = None
    typename = None
    online_user = None # 当前在线观看人数
    partition_index = None # 属于分P视频的索引
#不明：
    instant_server = None
    src = None
    partname = None
    allow_bp = None
    allow_feed = None
    created = None
#播放信息：
    play_site = None
    play_forward = None
    play_mobile = None

class Bangumi():
    def __init__(self):
        pass
    typeid = None
    lastupdate = None
    area = None
    bgmcount = None#番剧当前总集数
    title = None
    lastupdate_at = None
    attention = None #订阅数
    cover = None
    priority = None
    area = None
    weekday = None
    spid = None
    new = None
    scover = None
    mcover = None
    click = None
    coin = None
    season_id = None
    season_title = None
    click = None # 浏览数
    video_view = None
    episode_list = []
    tags = []
    isFinished = None
    newest_ep_id = None
    newest_ep_index = None

class Comment():
    def __init__(self):
        self.post_user = User()
    lv = None#楼层
    fbid = None#评论id
    parent_id = None #被回复留言ID
    msg = None
    ad_check = None#状态 (0: 正常 1: UP主隐藏 2: 管理员删除 3: 因举报删除)
    post_user = None
    like = None

class CommentList():
    def __init__(self):
        pass
    comments = None
    commentLen = None
    page = None

class ZhuantiInfo():
    def __init__(self, m_spid,m_title):
        self.spid = m_spid
        if isinstance(m_title,unicode):
            m_title = m_title.encode('utf8')
        self.title = m_title
    spid = None
    title = None
    author = None
    cover = None
    thumb = None
    ischeck = None #不明
    typeurl = None #总是"http://www.bilibili.com"
    tag = None
    description = None
    pubdate = None # 不明
    postdate = None
    lastupdate = None
    click = None
    favourite = None
    attention = None
    count = None
    bgmcount = None
    spcount = None
    season_id = None
    is_bangumi = None
    arcurl = None
    is_bangumi_end = None

class Danmu():
    def __init__(self):
        pass
    t_video = None
    t_stamp = None
    mid_crc = None  # 值为:hex(binascii.crc32(mid))
    danmu_type = None # 1:滚动弹幕 5：顶端弹幕  4：底部弹幕
    content = None
    danmu_color = None
    danmu_fontsize = None

class SponsorInfo():
    def __init__(self):
        pass
    bp = None  ## 剧番总B币
    percent = None  #承包总比例，不知道什么鬼
    ep_bp = None  ## 该话的B币
    ep_percent = None  ## 不明
    sponsor_num = None   ## 承包人数
    sponsor_user = None  ## 承包人列表

class LivingInfo():
    def __init__(self):
        pass
    url = None
    title = None
    cover = None
    mid = None  