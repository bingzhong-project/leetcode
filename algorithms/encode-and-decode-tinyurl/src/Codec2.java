import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.HashMap;
import java.util.Map;

public class Codec2 {

    private final String host = "http://tinyurl.com/";

    private final Map<String, String> urlMap = new HashMap<>();

    private String[] chars = new String[]{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e",
            "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"};

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(longUrl.getBytes());
            byte[] secretBytes = md.digest();
            StringBuilder md5code = new StringBuilder(new BigInteger(1, secretBytes).toString(16));
            for (int i = 0; i <= 32 - md5code.length(); i++) {
                md5code.insert(0, "0");
            }

            for (int i = 0; i < 4; i++) {
                String sub = md5code.substring(i * 8, i * 8 + 8);
                long hex = 0x3fffffff & Long.parseLong(sub, 16);
                StringBuilder shortUrl = new StringBuilder();
                for (int j = 0; j < 6; j++) {
                    long index = 0x3d & hex;
                    shortUrl.append(chars[(int) index]);
                    hex >>= 5;
                }
                if(!urlMap.containsKey(host + shortUrl)) {
                    urlMap.put(host + shortUrl, longUrl);
                    return host + shortUrl;
                }
            }

            throw new RuntimeException("conflict");
        } catch (Exception e) {
            throw new RuntimeException("error", e);
        }
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return urlMap.get(shortUrl);
    }
}
