package com.jfrog.bk.example;

import java.io.File;
/**
 */
public class Utils {

    public static int add(int a, int b) {
        return a + b;
    }
    
    public static void makeDirs(String path) {
        File fd = new File(path);
        if (!fd.exists()) {
            fd.mkdirs();
        }
    }

}
