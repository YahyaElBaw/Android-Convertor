package com.example.currencyconverter

import org.junit.Assert.assertEquals
import org.junit.Test

/**
 * Tests unitaires validant l'ensemble des scénarios de conversion du TP Currency Converter.
 */
class CurrencyConverterTest {

    @Test
    fun testCas1_UsdVersEur() {
        // 120 USD vers EUR -> 102.56
        val res = CurrencyConverter.convertir(120.0, "USD", "EUR")
        assertEquals("102.56", CurrencyConverter.formater(res))
    }

    @Test
    fun testCas2_EurVersTnd() {
        // 100 EUR vers TND -> 340.00
        val res = CurrencyConverter.convertir(100.0, "EUR", "TND")
        assertEquals("340.00", CurrencyConverter.formater(res))
    }

    @Test
    fun testCas3_GbpVersUsd() {
        // 50 GBP vers USD -> 67.24
        // 50 / 0.87 * 1.17 = 67.241379...
        val res = CurrencyConverter.convertir(50.0, "GBP", "USD")
        assertEquals("67.24", CurrencyConverter.formater(res))
    }

    @Test
    fun testCas4_Identiques() {
        // 10 EUR vers EUR -> 10.00
        val res = CurrencyConverter.convertir(10.0, "EUR", "EUR")
        assertEquals("10.00", CurrencyConverter.formater(res))
    }

    @Test
    fun testFormatageDeuxDecimales() {
        assertEquals("5.50", CurrencyConverter.formater(5.5))
        assertEquals("12.00", CurrencyConverter.formater(12.0))
        assertEquals("99.99", CurrencyConverter.formater(99.989))
    }
}
