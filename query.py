# coding=utf-8
import urllib.parse
import urllib.request
import json
import sys
import os
import codecs

if __name__ == '__main__':
    # init output file
    f_out = open("result.txt", 'wb')
    f_out.close()
    # process every file
    ct_all = 0
    for root, dirs, files in os.walk(sys.argv[1]):
        for name in files:
            f_name = root + '/' + name
            # open the file
            f_file = codecs.open(f_name, 'r', 'utf-8')
            ct_file = 0
            cur_line = ""
            # this file
            while cur_line != "EF":
                # init strs
                r_doi = ""
                r_title = ""
                f_title = False
                r_author = ""
                f_author = False
                r_info = ""
                r_abstract = ""
                r_keywords = ""
                f_keywords = False
                r_u1 = ""
                r_u2 = ""
                r_posts = r_delicious = r_fbwalls = r_feeds = r_forum = r_gplus = r_linkedin = "0"
                r_msm = r_peer_review_sites = r_pinners = r_policies = r_qs = r_rdts = "0"
                r_rh = r_tweeters = r_videos = r_weibo = r_wikipedia = "0"
                # deal with the data
                # this part
                cur_line = f_file.readline().strip('\r\n')
                while cur_line != "ER" and cur_line != "EF":
                    # author
                    if cur_line[0:2] == 'AF':
                        r_author = cur_line[3:len(cur_line)]
                        f_author = True

                    # title
                    elif cur_line[0:2] == 'TI':
                        f_author = False
                        f_title = True
                        r_title = cur_line[3:len(cur_line)]

                    # keyword 1
                    elif cur_line[0:2] == 'DE':
                        f_title = False
                        f_keywords = True
                        r_keywords = cur_line[3:len(cur_line)]

                    # keyword 2
                    elif cur_line[0:2] == 'ID':
                        f_keywords = True
                        r_keywords = r_keywords + '; ' + cur_line[3:len(cur_line)]

                    # info replacement
                    elif cur_line[0:2] == 'RP':
                        r_info = cur_line[3:len(cur_line)]

                    # abstract
                    elif cur_line[0:2] == 'AB':
                        r_abstract = cur_line[3:len(cur_line)]

                    # u1
                    elif cur_line[0:2] == 'U1':
                        r_u1 = cur_line[3:len(cur_line)]

                    # u2
                    elif cur_line[0:2] == 'U2':
                        r_u2 = cur_line[3:len(cur_line)]

                    # doi
                    elif cur_line[0:2] == 'DI':
                        r_doi = cur_line[3:len(cur_line)]

                    # multi-line things
                    elif cur_line[0:2] == '  ':
                        # author
                        if f_author:
                            r_author = r_author + "; " + cur_line[3:len(cur_line)]
                        # title
                        elif f_title:
                            r_title = r_title + ' ' + cur_line[3:len(cur_line)]
                        # kw
                        elif f_keywords:
                            r_keywords = r_keywords + ' ' + cur_line[3:len(cur_line)]

                    # dont care
                    else:
                        f_author = f_title = f_keywords = False

                    cur_line = f_file.readline().strip('\r\n')
                if r_doi != "":
                    ct_all = ct_all + 1
                    ct_file = ct_file + 1
                    # query citis
                    # try the doi
                    html_url = "http://api.altmetric.com/v1/doi/" + r_doi
                    html_req = urllib.request.Request(html_url)
                    ok = True
                    html_res = None
                    try:
                        html_res = urllib.request.urlopen(html_req, timeout=3)
                    except:
                        print("Social Ref Not Found.")
                        ok = False
                    if ok:
                        html_raw = html_res.read()
                        html_bin = html_raw.decode("UTF8")
                        dic_json = json.loads(html_bin)
                        # print(dic_json['title'])
                        if 'cited_by_posts_count' in dic_json.keys():
                            r_posts = dic_json['cited_by_posts_count']
                        if 'cited_by_delicious_count' in dic_json.keys():
                            r_delicious = dic_json['cited_by_delicious_count']
                        if 'cited_by_fbwalls_count' in dic_json.keys():
                            r_fbwalls = dic_json['cited_by_fbwalls_count']
                        if 'cited_by_feeds_count' in dic_json.keys():
                            r_feeds = dic_json['cited_by_feeds_count']
                        if 'cited_by_forum_count' in dic_json.keys():
                            r_forum = dic_json['cited_by_forum_count']
                        if 'cited_by_gplus_count' in dic_json.keys():
                            r_forum = dic_json['cited_by_gplus_count']
                        if 'cited_by_linkedin_count' in dic_json.keys():
                            r_linkedin = dic_json['cited_by_linkedin_count']
                        if 'cited_by_msm_count' in dic_json.keys():
                            r_msm = dic_json['cited_by_msm_count']
                        if 'cited_by_peer_review_sites_count' in dic_json.keys():
                            r_peer_review_sites = dic_json['cited_by_peer_review_sites_count']
                        if 'cited_by_pinners_count' in dic_json.keys():
                            r_pinners = dic_json['cited_by_pinners_count']
                        if 'cited_by_policies_count' in dic_json.keys():
                            r_policies = dic_json['cited_by_policies_count']
                        if 'cited_by_qs_count' in dic_json.keys():
                            r_qs = dic_json['cited_by_qs_count']
                        if 'cited_by_rdts_count' in dic_json.keys():
                            r_rdts = dic_json['cited_by_rdts_count']
                        if 'cited_by_rh_count' in dic_json.keys():
                            r_rh = dic_json['cited_by_rh_count']
                        if 'cited_by_tweeters_count' in dic_json.keys():
                            r_tweeters = dic_json['cited_by_tweeters_count']
                        if 'cited_by_videos_count' in dic_json.keys():
                            r_videos = dic_json['cited_by_videos_count']
                        if 'cited_by_weibo_count' in dic_json.keys():
                            r_weibo = dic_json['cited_by_weibo_count']
                        if 'cited_by_wikipedia_count' in dic_json.keys():
                            r_wikipedia = dic_json['cited_by_wikipedia_count']

                    else:
                        r_posts = r_delicious = r_fbwalls = r_feeds = r_forum = r_gplus = r_linkedin = "n/a"
                        r_msm = r_peer_review_sites = r_pinners = r_pilicies = r_qs = r_rdts = "n/a"
                        r_rh = r_tweeters = r_videos = r_weibo = r_wikipedia = "n/a"

                    # write
                    print(ct_all, "in total,", ct_file, "in", f_name, '\t', r_doi)
                    f_out = open("result.txt", 'ab')
                    f_out.write((r_doi + '\n').encode(encoding='UTF8'))
                    f_out.write((r_title + '\n').encode(encoding='UTF8'))
                    f_out.write((r_author + '\n').encode(encoding='UTF8'))
                    f_out.write((r_info + '\n').encode(encoding='UTF8'))
                    f_out.write((r_abstract + '\n').encode(encoding='UTF8'))
                    f_out.write((r_keywords + '\n').encode(encoding='UTF8'))
                    f_out.write((r_u1 + '\n').encode(encoding='UTF8'))
                    f_out.write((r_u2 + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_posts) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_delicious) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_fbwalls) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_feeds) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_forum) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_gplus) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_linkedin) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_msm) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_peer_review_sites) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_pinners) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_policies) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_qs) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_rdts) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_rh) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_tweeters) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_videos) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_weibo) + '\n').encode(encoding='UTF8'))
                    f_out.write((str(r_wikipedia) + '\n').encode(encoding='UTF8'))
                    f_out.close()

            f_file.close()
