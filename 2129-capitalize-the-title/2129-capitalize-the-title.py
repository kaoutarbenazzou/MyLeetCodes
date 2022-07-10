class Solution:
    def capitalizeTitle(self, title: str) -> str:#
        title=title.split(' ')
        for i in range(len(title)):
            title[i]=title[i].lower()
            if len(title[i])>2:
                w=list(title[i])
                w[0]=w[0].upper()
                w=''.join(w)
                title[i]=w
        title=' '.join(title)
        return title
           