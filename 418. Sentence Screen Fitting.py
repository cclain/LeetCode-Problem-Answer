class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wordlen=[len(x) for x in sentence]
        for x in wordlen:
            if x>cols:
                return 0
        pos_row=1;
        pos_col=0;
        cnt=0;
        onelen=sum(wordlen)+len(wordlen);
        while pos_row<=rows:
            if (cols-pos_col)/onelen>1:
                col_repeat=(cols-pos_col)/onelen;
                if pos_col!=0:
                    pos_col=col_repeat*onelen+pos_col;
                else:
                    pos_col=col_repeat*onelen-1
                cnt=cnt+col_repeat    
                
            for x in wordlen:
                if pos_col!=0:
                    if pos_col+1+x<=cols:
                        pos_col=pos_col+1+x;
                    else:
                        pos_row=pos_row+1;
                        pos_col=x;
                        if pos_row>rows:
                            return cnt
                else:
                    pos_col=x
            cnt+=1;
            if pos_col+1+wordlen[0]>cols:
                full_round=rows/pos_row;
                cnt=cnt*full_round;
                pos_row=pos_row*full_round+1;
                pos_col=0;
                if pos_row>rows:
                    return cnt
                