"""Responses.

responses serve both testing purpose aswell as dynamic docstring replacement
"""

responses = {
    "_v3_forexlabs_calendar": {
        "url": "labs/v1/calendar",
        "params": {
            "period": 86400,
            "instrument": "EUR_USD"
        },
        "response": [
              {
                "impact": 3,
                "actual": "60.8",
                "title": "ISM Manufacturing",
                "timestamp": 1519916400,
                "region": "americas",
                "forecast": "59.5",
                "currency": "USD",
                "unit": "index",
                "market": "58.7",
                "previous": "59.1"
              }
        ]
    },
    "_v3_forexlabs_histposratios": {
        "url": "labs/v1/historical_position_ratios",
        "params": {
            "period": 86400,
            "instrument": "EUR_USD"
        },
        "response": {
              "data": {
                "EUR_USD": {
                  "data": [
                    [
                      1519924801,
                      44.22,
                      1.2209
                    ],
                    [
                      1519926001,
                      44.33,
                      1.221
                    ],
                    [
                      1519927200,
                      44.16,
                      1.2212
                    ],
                    [
                      1519928400,
                      44.2,
                      1.2209
                    ],
                    [
                      1519929601,
                      43.88,
                      1.2201
                    ],
                    [
                      1519930800,
                      44.15,
                      1.2197
                    ],
                    [
                      1519932000,
                      44.51,
                      1.2204
                    ],
                    [
                      1519933200,
                      44.55,
                      1.2233
                    ],
                    [
                      1519934401,
                      44.55,
                      1.2254
                    ],
                    [
                      1519935601,
                      44.08,
                      1.226
                    ],
                    [
                      1519936801,
                      43.67,
                      1.2264
                    ],
                    [
                      1519938001,
                      43.55,
                      1.2263
                    ],
                    [
                      1519939201,
                      43.25,
                      1.2261
                    ],
                    [
                      1519940401,
                      43.28,
                      1.2263
                    ],
                    [
                      1519941601,
                      43.39,
                      1.2267
                    ],
                    [
                      1519942801,
                      43.69,
                      1.227
                    ],
                    [
                      1519944001,
                      43.57,
                      1.2269
                    ],
                    [
                      1519945201,
                      43.68,
                      1.2272
                    ],
                    [
                      1519946400,
                      43.51,
                      1.2268
                    ],
                    [
                      1519947601,
                      43.53,
                      1.2267
                    ],
                    [
                      1519948801,
                      43.71,
                      1.2271
                    ],
                    [
                      1519950001,
                      43.66,
                      1.2265
                    ],
                    [
                      1519951201,
                      43.78,
                      1.2269
                    ],
                    [
                      1519952401,
                      43.86,
                      1.2273
                    ],
                    [
                      1519953600,
                      43.85,
                      1.2273
                    ],
                    [
                      1519954800,
                      43.81,
                      1.2271
                    ],
                    [
                      1519956001,
                      44,
                      1.2275
                    ],
                    [
                      1519957200,
                      43.89,
                      1.2274
                    ],
                    [
                      1519958401,
                      43.95,
                      1.2273
                    ],
                    [
                      1519959601,
                      43.93,
                      1.2273
                    ],
                    [
                      1519960800,
                      43.86,
                      1.2276
                    ],
                    [
                      1519962000,
                      44.02,
                      1.2278
                    ],
                    [
                      1519963200,
                      44.18,
                      1.228
                    ],
                    [
                      1519964401,
                      44.52,
                      1.2283
                    ],
                    [
                      1519965600,
                      44.19,
                      1.2281
                    ],
                    [
                      1519966801,
                      44.14,
                      1.2278
                    ],
                    [
                      1519968000,
                      43.93,
                      1.2276
                    ],
                    [
                      1519969201,
                      43.82,
                      1.2277
                    ],
                    [
                      1519970401,
                      43.77,
                      1.2279
                    ],
                    [
                      1519971601,
                      43.02,
                      1.2269
                    ],
                    [
                      1519972801,
                      42.99,
                      1.2265
                    ],
                    [
                      1519974001,
                      42.73,
                      1.2263
                    ],
                    [
                      1519975201,
                      42.22,
                      1.2262
                    ],
                    [
                      1519976400,
                      42.13,
                      1.2255
                    ],
                    [
                      1519977601,
                      42.02,
                      1.2263
                    ],
                    [
                      1519978801,
                      42.15,
                      1.2261
                    ],
                    [
                      1519980000,
                      42.5,
                      1.2273
                    ],
                    [
                      1519981201,
                      42.2,
                      1.2274
                    ],
                    [
                      1519982400,
                      42.06,
                      1.2271
                    ],
                    [
                      1519983600,
                      42.38,
                      1.2279
                    ],
                    [
                      1519984800,
                      42.29,
                      1.2276
                    ],
                    [
                      1519986000,
                      42.16,
                      1.2281
                    ],
                    [
                      1519987201,
                      43.46,
                      1.2291
                    ],
                    [
                      1519988401,
                      43.51,
                      1.2291
                    ],
                    [
                      1519989601,
                      43.4,
                      1.2317
                    ],
                    [
                      1519990800,
                      43.46,
                      1.2317
                    ],
                    [
                      1519992001,
                      43.07,
                      1.2304
                    ],
                    [
                      1519993201,
                      43.56,
                      1.2316
                    ],
                    [
                      1519994401,
                      43.75,
                      1.2319
                    ],
                    [
                      1519995601,
                      43.15,
                      1.2308
                    ],
                    [
                      1519996801,
                      42.94,
                      1.2309
                    ],
                    [
                      1519998001,
                      42.99,
                      1.2315
                    ],
                    [
                      1519999201,
                      42.33,
                      1.2309
                    ],
                    [
                      1520000400,
                      41.93,
                      1.2299
                    ],
                    [
                      1520001601,
                      42.31,
                      1.2303
                    ],
                    [
                      1520002801,
                      42.5,
                      1.2313
                    ],
                    [
                      1520004000,
                      42.8,
                      1.2326
                    ],
                    [
                      1520005201,
                      42.67,
                      1.2317
                    ],
                    [
                      1520006401,
                      42.29,
                      1.2309
                    ],
                    [
                      1520007600,
                      42.33,
                      1.2309
                    ],
                    [
                      1520008800,
                      42.63,
                      1.2321
                    ],
                    [
                      1520010001,
                      42.11,
                      1.2314
                    ]
                  ],
                  "label": "EUR/USD"
                }
              }
            }
    },
    "_v3_forexlabs_spreads": {
        "url": "labs/v1/spreads",
        "params": {
            "period": 57600,
            "instrument": "EUR_USD"
        },
        "response": {
              "max": [
                [
                  1520028000,
                  6
                ]
              ],
              "avg": [
                [
                  1520028000,
                  3.01822
                ]
              ],
              "min": [
                [
                  1520028000,
                  1.7
                ]
              ]
        }
    },
    "_v3_forexlabs_commoftrad": {
        "url": "labs/v1/commitments_of_traders",
        "params": {
            "instrument": "EUR_USD"
        },
        "response": {
            "EUR_USD": [
                {
                  "oi": "603460",
                  "price": "1.2315925",
                  "ncs": "109280",
                  "ncl": "258022",
                  "date": 1517288400,
                  "unit": "Contracts Of EUR 125,000"
                },
                {
                  "oi": "596937",
                  "price": "1.2364",
                  "ncs": "110546",
                  "ncl": "251369",
                  "date": 1517893200,
                  "unit": "Contracts Of EUR 125,000"
                },
                {
                  "oi": "564233",
                  "price": "1.2330275",
                  "ncs": "103496",
                  "ncl": "230785",
                  "date": 1518498000,
                  "unit": "Contracts Of EUR 125,000"
                },
                {
                  "oi": "567534",
                  "price": "1.2346025",
                  "ncs": "103147",
                  "ncl": "229273",
                  "date": 1519102800,
                  "unit": "Contracts Of EUR 125,000"
                },
                {
                  "oi": "567463",
                  "price": "1.23557",
                  "ncs": "100310",
                  "ncl": "238287",
                  "date": 1519707600,
                  "unit": "Contracts Of EUR 125,000"
                }
            ]
        }
    },
    "_v3_forexlabs_orderbookdata": {
        "url": "labs/v1/orderbook_data",
        "params": {
            "instrument": "EUR_USD",
            "period": 3600
        },
        "response": {
            "1520066400": {
                "rate": 1.2318,
                "price_points": {
                  "1.288": {
                    "ps": 0,
                    "ol": 0.0105,
                    "os": 0.0105,
                    "pl": 0
                  },
                  "1.23": {
                    "ps": 1.2155,
                    "ol": 0.3871,
                    "os": 0.2615,
                    "pl": 0.5633
                  },
                  "1.223": {
                    "ps": 1.1266,
                    "ol": 0.5021,
                    "os": 0.2197,
                    "pl": 0.3854
                  },
                  "1.1825": {
                    "ps": 0.1779,
                    "ol": 0.1465,
                    "os": 0.0628,
                    "pl": 0
                  },
                  "1.22": {
                    "ps": 0.9191,
                    "ol": 0.6486,
                    "os": 0.136,
                    "pl": 0.2965
                  },
                  "1.2245": {
                    "ps": 0.5336,
                    "ol": 0.5021,
                    "os": 0.3975,
                    "pl": 0.4447
                  },
                  "1.2085": {
                    "ps": 0.1482,
                    "ol": 0.2092,
                    "os": 0.2197,
                    "pl": 0.1482
                  },
                  "1.26": {
                    "ps": 0,
                    "ol": 0.2197,
                    "os": 0.68,
                    "pl": 0
                  },
                  "1.25": {
                    "ps": 0.0593,
                    "ol": 0.272,
                    "os": 1.0566,
                    "pl": 0.1186
                  },
                  "1.24": {
                    "ps": 0.1186,
                    "ol": 0.4289,
                    "os": 0.8264,
                    "pl": 0.4447
                  }
                }
            }
        }
    },
    "_v3_forexlabs_autochartist": {
        "url": "labs/v1/signal/autochartist",
        "params": {
            "instrument": "EUR_JPY"
        },
        "response": {
            "1520066400": {
                "rate": 1.2318,
                "price_points": {
                  "1.288": {
                    "ps": 0,
                    "ol": 0.0105,
                    "os": 0.0105,
                    "pl": 0
                  },
                  "1.23": {
                    "ps": 1.2155,
                    "ol": 0.3871,
                    "os": 0.2615,
                    "pl": 0.5633
                  },
                  "1.223": {
                    "ps": 1.1266,
                    "ol": 0.5021,
                    "os": 0.2197,
                    "pl": 0.3854
                  },
                  "1.1825": {
                    "ps": 0.1779,
                    "ol": 0.1465,
                    "os": 0.0628,
                    "pl": 0
                  },
                  "1.22": {
                    "ps": 0.9191,
                    "ol": 0.6486,
                    "os": 0.136,
                    "pl": 0.2965
                  },
                  "1.2245": {
                    "ps": 0.5336,
                    "ol": 0.5021,
                    "os": 0.3975,
                    "pl": 0.4447
                  },
                  "1.2085": {
                    "ps": 0.1482,
                    "ol": 0.2092,
                    "os": 0.2197,
                    "pl": 0.1482
                  },
                  "1.26": {
                    "ps": 0,
                    "ol": 0.2197,
                    "os": 0.68,
                    "pl": 0
                  },
                  "1.25": {
                    "ps": 0.0593,
                    "ol": 0.272,
                    "os": 1.0566,
                    "pl": 0.1186
                  },
                  "1.24": {
                    "ps": 0.1186,
                    "ol": 0.4289,
                    "os": 0.8264,
                    "pl": 0.4447
                  }
                }
            }
        }
    },
}
#     "_v3_accounts_accountID_openpositions": {
#         "url": "v3/accounts/{accountID}/positions",
#         "response": {
#             "positions": [
#                 {
#                     "short": {
#                         "units": "0",
#                         "resettablePL": "-14164.3000",
#                         "unrealizedPL": "0.0000",
#                         "pl": "-14164.3000"
#                     },
#                     "unrealizedPL": "-284.0000",
#                     "long": {
#                         "unrealizedPL": "-284.0000",
#                         "units": "10",
#                         "resettablePL": "404.5000",
#                         "tradeIDs": [
#                             "2315"
#                         ],
#                         "averagePrice": "10678.3",
#                         "pl": "404.5000"
#                     },
#                     "instrument": "DE30_EUR",
#                     "resettablePL": "-13759.8000",
#                     "pl": "-13759.8000"
#                 },
#                 {
#                     "short": {
#                         "unrealizedPL": "-0.0738",
#                         "units": "-100",
#                         "resettablePL": "0.0000",
#                         "tradeIDs": [
#                             "2323"
#                         ],
#                         "averagePrice": "1.09843",
#                         "pl": "0.0000"
#                     },
#                     "unrealizedPL": "-0.0738",
#                     "long": {
#                         "units": "0",
#                         "resettablePL": "-44.6272",
#                         "unrealizedPL": "0.0000",
#                         "pl": "-44.6272"
#                     },
#                     "instrument": "EUR_USD",
#                     "resettablePL": "-44.6272",
#                     "pl": "-44.6272"
#                 }
#             ],
#             "lastTransactionID": "2327"
#         }
#     },
#     "_v3_accounts_accountID_positiondetails": {
#         "url": "v3/accounts/{accountID}/positions/{instrument}",
#         "response": {
#             "position": {
#                 "short": {
#                     "unrealizedPL": "-0.0738",
#                     "units": "-100",
#                     "resettablePL": "0.0000",
#                     "tradeIDs": [
#                         "2323"
#                     ],
#                     "averagePrice": "1.09843",
#                     "pl": "0.0000"
#                 },
#                 "unrealizedPL": "-0.0738",
#                 "long": {
#                     "units": "0",
#                     "resettablePL": "-44.6272",
#                     "unrealizedPL": "0.0000",
#                     "pl": "-44.6272"
#                 },
#                 "instrument": "EUR_USD",
#                 "resettablePL": "-44.6272",
#                 "pl": "-44.6272"
#             },
#             "lastTransactionID": "2327"
#         }
#     },
#     "_v3_accounts_accountID_position_close": {
#         "url": "v3/accounts/{accountID}/positions/{instrument}/close",
#         "body": {
#             "longUnits": "ALL"
#         },
#         "response": {
#             "lastTransactionID": "6391",
#             "longOrderCreateTransaction": {
#                 "accountID": "<ACCOUNT>",
#                 "batchID": "6390",
#                 "id": "6390",
#                 "instrument": "EUR_USD",
#                 "longPositionCloseout": {
#                     "instrument": "EUR_USD",
#                     "units": "ALL"
#                 },
#                 "positionFill": "REDUCE_ONLY",
#                 "reason": "POSITION_CLOSEOUT",
#                 "time": "2016-06-22T18:41:35.034041665Z",
#                 "timeInForce": "FOK",
#                 "type": "MARKET_ORDER",
#                 "units": "-251",
#                 "userID": "<USERID>"
#             },
#             "longOrderFillTransaction": {
#                 "accountBalance": "43650.69807",
#                 "accountID": "<ACCOUNT>",
#                 "batchID": "6390",
#                 "financing": "0.00000",
#                 "id": "6391",
#                 "instrument": "EUR_USD",
#                 "orderID": "6390",
#                 "pl": "-0.03370",
#                 "price": "1.13018",
#                 "reason": "MARKET_ORDER_POSITION_CLOSEOUT",
#                 "time": "2016-06-22T18:41:35.034041665Z",
#                 "tradesClosed": [
#                     {
#                         "financing": "0.00000",
#                         "realizedPL": "-0.00013",
#                         "tradeID": "6383",
#                         "units": "-1"
#                     },
#                     {
#                         "financing": "0.00000",
#                         "realizedPL": "-0.03357",
#                         "tradeID": "6385",
#                         "units": "-250"
#                     }
#                 ],
#                 "type": "ORDER_FILL",
#                 "units": "-251",
#                 "userID": "<USERID>"
#             },
#             "relatedTransactionIDs": [
#                 "6390",
#                 "6391"
#             ]
#         }
#     }
