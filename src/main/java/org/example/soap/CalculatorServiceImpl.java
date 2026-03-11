package org.example.soap;

import javax.jws.WebService;

@WebService(endpointInterface = "org.example.soap.CalculatorService")
public class CalculatorServiceImpl implements CalculatorService {

    @Override
    public int add(int num1, int num2) {
        return num1 + num2;
    }
}