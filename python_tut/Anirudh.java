import java.io.*;

class Anirudh 
{

    public static void main(String[]args)
    {
        String words[]={"anirudh","pandey"};
        String sentence=sentence(words);
        System.out.println(sentence);
    }
    public static String sentence (String[]words)
    {
        String sentence="";
        for (String x : words) 
        {
            sentence=sentence+x;
        } 
        return sentence;
    }

}