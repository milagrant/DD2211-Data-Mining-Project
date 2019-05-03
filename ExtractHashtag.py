import pandas as pd
import os
import glob
import re

def extract_top_hashtag():

	curr_path = os.path.dirname(os.path.realpath(__file__))
	ego_nodes = [int(x.split("/twitter\\")[-1].split('.')[0]) for x in glob.glob("%s/dataset/twitter/*.featnames" % (curr_path,))]
	node_list = []
	df_hashtag = pd.DataFrame()

	for ego_node in ego_nodes:
	    #print(ego_node)
	    feat_names_file = open(curr_path+'/dataset/twitter/%d.featnames' % (ego_node), 'r', encoding='utf8')
	    hashtag = []
	    for line in feat_names_file:
	        split = line.split(" ")
	        feat_name = split[1].rstrip()
	        if '#' in feat_name:
	            hashtag.append(feat_name)
	    feat_names_file.close()
	    
	    df_hashtag_temp = pd.DataFrame(hashtag, columns=['hashtag'])
	    list_hashtag = []
	    
	    ego_feat = open(curr_path+'/dataset/twitter/%d.egofeat' % (ego_node), 'r')
	    for line in ego_feat:
	        line = line.rstrip()
	        split = [int(x) for x in line.split(' ')]
	        features = split[0:len(hashtag)]
	        list_hashtag.append(features)
	    ego_feat.close()
	    
	    features_file = open(curr_path+'/dataset/twitter/%d.feat' % (ego_node), 'r')
	    for line in features_file:
	        line = line.rstrip()
	        split = [int(x) for x in line.split(' ')]
	        node_id = split[0]
	        if node_id not in node_list:
	            node_list.append(node_id)
	            features = split[1:len(hashtag)+1]
	            list_hashtag.append(features)
	    features_file.close()
	    
	    list_hashtag = list(map(list, zip(*list_hashtag)))
	    sum_hashtag = [sum(i) for i in list_hashtag]
	    df_hashtag_temp['count'] = sum_hashtag
	    
	    df_hashtag = df_hashtag.append(df_hashtag_temp, ignore_index=True)

	df_final = df_hashtag.copy()
	df_final['hashtag'] = df_final['hashtag'].str.lower()
	df_final['hashtag'] = df_final['hashtag'].map(lambda x: re.sub(r'\W+', '', x))
	df_final = df_final[df_final['hashtag']!='']
	df_final = pd.DataFrame(df_final.groupby(by='hashtag')['count'].sum()).reset_index()
	df_final = df_final[df_final['count'] >= 100]
	df_final = df_final[df_final['hashtag'].apply(lambda x: x.isnumeric() == False)]
	df_final.sort_values(by='count', ascending=False, inplace=True)
	df_final.reset_index(drop=True, inplace=True)

	df_final.to_csv('dataset/top_hashtag.csv', index=False)

if __name__ == '__main__':
	print("Extracting Top Hashtag")
	extract_top_hashtag()
	print("Finish!")