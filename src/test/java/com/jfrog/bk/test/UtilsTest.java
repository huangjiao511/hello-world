package com.jfrog.bk.test;

import com.jfrog.bk.example.Utils;
import org.junit.Assert;
import org.junit.Ignore;
import org.junit.Test;

/**
 * Created by xxxx on 2017/6/28.
 */
public class UtilsTest {
    @Test
    public void addTest1() {
        Assert.assertTrue(Utils.add(1,2) == 3);
    }

    @Test
    public void addTest2() {
        Assert.assertEquals(Utils.add(1,2),3);
    }

    @Test
    public void addTest3() {
        Assert.assertEquals(Utils.add(1,1),3);
    }
}
