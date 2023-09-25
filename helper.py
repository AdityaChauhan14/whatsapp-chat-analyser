def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    if selected_user == 'Overall':
        #fetch msgs
        num_messages = df.shape[0]
        #fetch words
        words = []
        for message in df['message']:
            words.extend(message.split())
        return num_messages, len(words)
    else:
        new_df = df[df['user'] == selected_user]
        num_messages = new_df.shape[0]
        # return .shape[0]
        words = []
        for message in new_df['message']:
            words.extend(message.split())
        return num_messages, len(words)


