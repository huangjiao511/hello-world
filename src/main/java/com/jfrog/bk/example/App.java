package com.jfrog.bk.example;

import org.apache.log4j.PropertyConfigurator;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.embedded.ConfigurableEmbeddedServletContainer;
import org.springframework.boot.context.embedded.EmbeddedServletContainerCustomizer;
import org.springframework.boot.context.web.SpringBootServletInitializer;
import org.springframework.stereotype.Controller;

/**
 * Hello world!
 *
 */
@SpringBootApplication
@Controller
public class App extends SpringBootServletInitializer {

    public static void main(String[] args) {
        if(true){
            String str = "foo";
        }
		
		if(false)
		{
            String str = "fooxxx";
        }
        
        SpringApplication.run(App.class, args);
    }

}
