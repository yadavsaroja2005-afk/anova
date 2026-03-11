package org.example.soap;

import org.apache.cxf.jaxws.JaxWsProxyFactoryBean;

public class CalculatorClient {

    public static void main(String[] args) {

        JaxWsProxyFactoryBean factory = new JaxWsProxyFactoryBean();

        factory.setServiceClass(CalculatorService.class);
        factory.setAddress("http://localhost:8080/calculator");

        CalculatorService calculator = (CalculatorService) factory.create();

        int result = calculator.add(10, 20);

        System.out.println("Result: " + result);
    }
}