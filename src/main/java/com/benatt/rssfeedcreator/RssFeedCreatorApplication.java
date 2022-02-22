package com.benatt.rssfeedcreator;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class RssFeedCreatorApplication {

	public static void main(String[] args) {
		SpringApplication.run(RssFeedCreatorApplication.class, args);
	}

}
