import java.util.HashMap;

public class SlidingWindowTemplate {


    public static void main (String[] arg) {


        System.out.println("hello");
    }


    public static void SlidingWindow(String s, String[] words) {

        // Usually you will have a list of words or a word trying to match a string 
        // First start off with the begin and end

        int begin = 0;
        int end = 0; 
        // This counter will be used for the small loop and incrememnt begin
        int counter =0;
        HashMap<String, Integer> countMap = new HashMap<>();
        // Add words to a hashmap counter
        for (String word: words) {
            countMap.put(word, countMap.getOrDefault(word, 0) +1);
        }

        // counter is usually hm.size(), or it could be some other
        counter = countMap.size();
        
        // the first loop moving end pointer
        while (end < s.length()) {

            String someMatchUsingEnd = "";
            if (countMap.containsKey(someMatchUsingEnd)) {
                countMap.put(someMatchUsingEnd, countMap.get(someMatchUsingEnd) -1);
                counter--;
            }


                // move end pointer forward
            end++;


            while (counter ==0) {

                String someMatchUsingBegin = "";
                if (countMap.containsKey(someMatchUsingBegin)) {
                    countMap.put(someMatchUsingBegin, countMap.get(someMatchUsingBegin) +1);
                    counter++;
                }

                    // move begin pointer forward
                begin++;

                    // Add to result here
                    // res.add(someRes);

                }


        }




    }
    
}
