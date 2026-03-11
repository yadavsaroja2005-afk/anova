package org.example.soap;

import org.apache.cxf.jaxws.JaxWsServerFactoryBean;

public class CalculatorPublisher {

    public static void main(String[] args) {

        JaxWsServerFactoryBean factory = new JaxWsServerFactoryBean();

        factory.setServiceClass(CalculatorServiceImpl.class);
        factory.setAddress("http://localhost:8080/calculator");

        factory.create();

        System.out.println("Service running at http://localhost:8080/calculator");
    }
}