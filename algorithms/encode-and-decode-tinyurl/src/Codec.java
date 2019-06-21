import java.net.URI;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

public class Codec {

    private final String host = "http://tinyurl.com/";

    private Map<String, String> urlMap = new HashMap<>();

    private AtomicLong counter = new AtomicLong(916132832L);

    private List<String> charList = Arrays.asList(new String[] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a",
            "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "T", "U", "V", "W", "X", "Y", "Z" });

    {
        Collections.shuffle(charList);
    }

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        String shortUrl = "";
        long count = counter.getAndIncrement();
        while (count > 0) {
            int mod = (int) count % 62;
            count /= 62;
            shortUrl = charList.get(mod) + shortUrl;
        }

        shortUrl = host + shortUrl;
        urlMap.put(shortUrl, longUrl);

        return shortUrl;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return urlMap.get(shortUrl);
    }
}
