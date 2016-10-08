var labelType, useGradients, nativeTextSupport, animate;

(function() {
  var ua = navigator.userAgent,
      iStuff = ua.match(/iPhone/i) || ua.match(/iPad/i),
      typeOfCanvas = typeof HTMLCanvasElement,
      nativeCanvasSupport = (typeOfCanvas == 'object' || typeOfCanvas == 'function'),
      textSupport = nativeCanvasSupport 
        && (typeof document.createElement('canvas').getContext('2d').fillText == 'function');
  //I'm setting this based on the fact that ExCanvas provides text support for IE
  //and that as of today iPhone/iPad current text support is lame
  labelType = (!nativeCanvasSupport || (textSupport && !iStuff))? 'Native' : 'HTML';
  nativeTextSupport = labelType == 'Native';
  useGradients = nativeCanvasSupport;
  animate = !(iStuff || !nativeCanvasSupport);
})();

var Log = {
  elem: false,
  write: function(text){
    if (!this.elem) 
      this.elem = document.getElementById('log');
    this.elem.innerHTML = text;
    this.elem.style.left = (500 - this.elem.offsetWidth / 2) + 'px';
  }
};


function init(){
    //init data    
    
	var json = {	
        "name": "Káin",
        "id": "1",
        "children": [
            {
                "name": "Enoch, a Bölcs",
                "id": "2",
                "sire": "1",
                "children": [
                    {
                        "name": "Veddhartha",
                        "id": "3",
                        "sire": "2",
                        "children": [
                            {
                                "name": "Ur-i Arakur",
                                "id": "4",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Nefertum",
                                        "id": "5",
                                        "sire": "4",
                                        "children": [
                                            {
                                                "name": "Egyiptomi Ventruek",
                                                "id": "6",
                                                "sire": "5"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Ur-i Tiamat",
                                        "id": "7",
                                        "sire": "4",
                                        "children": [
                                            {
                                                "name": "Gotsdam",
                                                "id": "8",
                                                "sire": "7",
                                                "children": [
                                                    {
                                                        "name": "Dylan",
                                                        "id": "9",
                                                        "sire": "8"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Severus",
                                                "id": "10",
                                                "sire": "7",
                                                "children": [
                                                    {
                                                        "name": "Lucinde",
                                                        "id": "11",
                                                        "sire": "10"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Ishrafel",
                                                "id": "12",
                                                "sire": "7",
                                                "children": [
                                                    {
                                                        "name": "Malachi Faruq",
                                                        "id": "13",
                                                        "sire": "12"
                                                    },
                                                    {
                                                        "name": "Mustafa",
                                                        "id": "14",
                                                        "sire": "12",
                                                        "children": [
                                                            {
                                                                "name": "Abdul Rahman",
                                                                "id": "15",
                                                                "sire": "14",
                                                                "children": [
                                                                    {
                                                                        "name": "Shayke Muhammad",
                                                                        "id": "16",
                                                                        "sire": "15"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Török Ventruek",
                                                                "id": "17",
                                                                "sire": "14"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Amon Ho-tepe / Hoteph",
                                                        "id": "18",
                                                        "sire": "12",
                                                        "children": [
                                                            {
                                                                "name": "Angol Ventruek",
                                                                "id": "19",
                                                                "sire": "18"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Summer Ventruek",
                                                "id": "20",
                                                "sire": "7"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Medon",
                                "id": "21",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Görög Ventruek",
                                        "id": "22",
                                        "sire": "21"
                                    },
                                    {
                                        "name": "Gaius Fabricius",
                                        "id": "23",
                                        "sire": "21",
                                        "children": [
                                            {
                                                "name": "Francia Ventruek",
                                                "id": "24",
                                                "sire": "23"
                                            },
                                            {
                                                "name": "Bartholomeo",
                                                "id": "25",
                                                "sire": "23",
                                                "children": [
                                                    {
                                                        "name": "Olasz Ventruek",
                                                        "id": "26",
                                                        "sire": "25"
                                                    },
                                                    {
                                                        "name": "Gawain",
                                                        "id": "27",
                                                        "sire": "25",
                                                        "children": [
                                                            {
                                                                "name": "Kelta Ventruek",
                                                                "id": "28",
                                                                "sire": "27"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Michaela",
                                                        "id": "29",
                                                        "sire": "25",
                                                        "children": [
                                                            {
                                                                "name": "Tabitha Bauer",
                                                                "id": "30",
                                                                "sire": "29"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Nefer-meri-Isis",
                                "id": "31",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Elihu",
                                        "id": "32",
                                        "sire": "31",
                                        "children": [
                                            {
                                                "name": "Rebekah",
                                                "id": "33",
                                                "sire": "32",
                                                "children": [
                                                    {
                                                        "name": "Kánaánita Ventruek",
                                                        "id": "34",
                                                        "sire": "33"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Stalest Coursain",
                                                "id": "35",
                                                "sire": "32",
                                                "children": [
                                                    {
                                                        "name": "Guillame de Tulede",
                                                        "id": "36",
                                                        "sire": "35"
                                                    },
                                                    {
                                                        "name": "Catherine von Hawthorne",
                                                        "id": "37",
                                                        "sire": "35",
                                                        "children": [
                                                            {
                                                                "name": "Német Ventruek",
                                                                "id": "38",
                                                                "sire": "37"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Alexander Vargos",
                                        "id": "39",
                                        "sire": "31",
                                        "children": [
                                            {
                                                "name": "Godefroy",
                                                "id": "40",
                                                "sire": "39",
                                                "children": [
                                                    {
                                                        "name": "Skandináv Ventruek",
                                                        "id": "41",
                                                        "sire": "40"
                                                    },
                                                    {
                                                        "name": "Titus",
                                                        "id": "42",
                                                        "sire": "40",
                                                        "children": [
                                                            {
                                                                "name": "Dominique",
                                                                "id": "43",
                                                                "sire": "42"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Spártai Artemisz",
                                "id": "44",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Lysander",
                                        "id": "45",
                                        "sire": "44",
                                        "children": [
                                            {
                                                "name": "Evarchus",
                                                "id": "46",
                                                "sire": "45"
                                            },
                                            {
                                                "name": "Gnaeus",
                                                "id": "47",
                                                "sire": "45",
                                                "children": [
                                                    {
                                                        "name": "Junius",
                                                        "id": "48",
                                                        "sire": "47",
                                                        "children": [
                                                            {
                                                                "name": "Spanyol Ventruek",
                                                                "id": "49",
                                                                "sire": "48"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Gaius Cassius",
                                                "id": "50",
                                                "sire": "45",
                                                "children": [
                                                    {
                                                        "name": "Lucius Trebius Rufus",
                                                        "id": "51",
                                                        "sire": "50",
                                                        "children": [
                                                            {
                                                                "name": "Province-i Leucruy",
                                                                "id": "52",
                                                                "sire": "51",
                                                                "children": [
                                                                    {
                                                                        "name": "Keresztes Ventruek",
                                                                        "id": "53",
                                                                        "sire": "52"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Marseilles-i Vicelin",
                                                                "id": "54",
                                                                "sire": "51"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Római Ventruek",
                                                        "id": "55",
                                                        "sire": "50"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Z'avier S'ren",
                                                "id": "56",
                                                "sire": "45"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Michaellis",
                                        "id": "57",
                                        "sire": "44"
                                    }
                                ]
                            },
                            {
                                "name": "Tinia",
                                "id": "58",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Collat",
                                        "id": "59",
                                        "sire": "58",
                                        "children": [
                                            {
                                                "name": "Camilla",
                                                "id": "60",
                                                "sire": "59"
                                            },
                                            {
                                                "name": "Lyle",
                                                "id": "61",
                                                "sire": "59",
                                                "children": [
                                                    {
                                                        "name": "Amerikai Ventruek",
                                                        "id": "62",
                                                        "sire": "61"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Julia Antasia",
                                        "id": "63",
                                        "sire": "58",
                                        "children": [
                                            {
                                                "name": "Barbarossa",
                                                "id": "64",
                                                "sire": "63"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Etrusz Ventruek",
                                        "id": "65",
                                        "sire": "58"
                                    }
                                ]
                            },
                            {
                                "name": "Aken Hoten",
                                "id": "66",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Athéni Helena",
                                        "id": "67",
                                        "sire": "66",
                                        "children": [
                                            {
                                                "name": "Cyrene-i Sára",
                                                "id": "68",
                                                "sire": "67",
                                                "children": [
                                                    {
                                                        "name": "Skóciai Anguselus",
                                                        "id": "69",
                                                        "sire": "68",
                                                        "children": [
                                                            {
                                                                "name": "Skót Ventruek",
                                                                "id": "70",
                                                                "sire": "69"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Horatio Vallengard",
                                                        "id": "71",
                                                        "sire": "68",
                                                        "children": [
                                                            {
                                                                "name": "Kyle Strathcona",
                                                                "id": "72",
                                                                "sire": "71",
                                                                "children": [
                                                                    {
                                                                        "name": "Kanadia Ventruek",
                                                                        "id": "73",
                                                                        "sire": "72"
                                                                    },
                                                                    {
                                                                        "name": "Philippe Sainte-Lauctrec",
                                                                        "id": "74",
                                                                        "sire": "72"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Sabine Rothschilde",
                                                        "id": "75",
                                                        "sire": "68",
                                                        "children": [
                                                            {
                                                                "name": "Deutsch Ábrahám",
                                                                "id": "76",
                                                                "sire": "75",
                                                                "children": [
                                                                    {
                                                                        "name": "Deutsch-Hatvany Janka",
                                                                        "id": "77",
                                                                        "sire": "76",
                                                                        "children": [
                                                                            {
                                                                                "name": "Deutsch Antónia",
                                                                                "id": "78",
                                                                                "sire": "77",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Hatvany Alexander",
                                                                                        "id": "79",
                                                                                        "sire": "78"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Miguel de Aguerrila",
                                                "id": "80",
                                                "sire": "67",
                                                "children": [
                                                    {
                                                        "name": "Sebastiao de Avis",
                                                        "id": "81",
                                                        "sire": "80",
                                                        "children": [
                                                            {
                                                                "name": "Portugál Ventruek",
                                                                "id": "82",
                                                                "sire": "81"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Arturo San Gerande",
                                                        "id": "83",
                                                        "sire": "80",
                                                        "children": [
                                                            {
                                                                "name": "Gyarmati Ventruek",
                                                                "id": "84",
                                                                "sire": "83"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Nathaniel van Hooves",
                                                "id": "85",
                                                "sire": "67",
                                                "children": [
                                                    {
                                                        "name": "Holland Ventruek",
                                                        "id": "86",
                                                        "sire": "85"
                                                    },
                                                    {
                                                        "name": "Brazil Ventruek",
                                                        "id": "87",
                                                        "sire": "85"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Johannes Castelein",
                                                "id": "88",
                                                "sire": "67",
                                                "children": [
                                                    {
                                                        "name": "Arjan Voorhies",
                                                        "id": "89",
                                                        "sire": "88"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Marcus Antonius",
                                "id": "90",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Caius",
                                        "id": "91",
                                        "sire": "90",
                                        "children": [
                                            {
                                                "name": "Epirus",
                                                "id": "92",
                                                "sire": "91",
                                                "children": [
                                                    {
                                                        "name": "Bizánci Ventruek",
                                                        "id": "93",
                                                        "sire": "92"
                                                    },
                                                    {
                                                        "name": "Marcus Vitel",
                                                        "id": "94",
                                                        "sire": "92"
                                                    },
                                                    {
                                                        "name": "Ashton",
                                                        "id": "95",
                                                        "sire": "92"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Democritus",
                                                "id": "96",
                                                "sire": "91"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Belisarius",
                                        "id": "97",
                                        "sire": "90",
                                        "children": [
                                            {
                                                "name": "Tonuzoba (Tanis-Aba)",
                                                "id": "98",
                                                "sire": "97",
                                                "children": [
                                                    {
                                                        "name": "Árpádházi Zombor",
                                                        "id": "99",
                                                        "sire": "98",
                                                        "children": [
                                                            {
                                                                "name": "Petronilla",
                                                                "id": "100",
                                                                "sire": "99",
                                                                "children": [
                                                                    {
                                                                        "name": "Temesvári János",
                                                                        "id": "101",
                                                                        "sire": "100",
                                                                        "children": [
                                                                            {
                                                                                "name": "Zlatan Pasi",
                                                                                "id": "102",
                                                                                "sire": "101",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "dr. Berenkúti Sándor",
                                                                                        "id": "103",
                                                                                        "sire": "102"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "Szabina",
                                                                        "id": "104",
                                                                        "sire": "100",
                                                                        "children": [
                                                                            {
                                                                                "name": "Siskovits András",
                                                                                "id": "105",
                                                                                "sire": "104",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Ciprián pap",
                                                                                        "id": "106",
                                                                                        "sire": "105"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Árpádházi IV. Kun László",
                                                                "id": "107",
                                                                "sire": "99",
                                                                "children": [
                                                                    {
                                                                        "name": "Tomori Pál",
                                                                        "id": "108",
                                                                        "sire": "107",
                                                                        "children": [
                                                                            {
                                                                                "name": "Nádasi Tersztyánszky Tivadar",
                                                                                "id": "109",
                                                                                "sire": "108"
                                                                            },
                                                                            {
                                                                                "name": "Hunyadi Karolin",
                                                                                "id": "110",
                                                                                "sire": "108"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "báró Aba Tamás",
                                                                        "id": "111",
                                                                        "sire": "107",
                                                                        "children": [
                                                                            {
                                                                                "name": "gróf Zichy István",
                                                                                "id": "112",
                                                                                "sire": "111"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Albrecht Tivadar",
                                                                "id": "113",
                                                                "sire": "99",
                                                                "children": [
                                                                    {
                                                                        "name": "Szendi-Literáti Anna",
                                                                        "id": "114",
                                                                        "sire": "113",
                                                                        "children": [
                                                                            {
                                                                                "name": "Anton von Hohenzollern-Hechingen",
                                                                                "id": "115",
                                                                                "sire": "114",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Engelhard Alíz",
                                                                                        "id": "116",
                                                                                        "sire": "115"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Bölcs Károly",
                                                "id": "117",
                                                "sire": "97",
                                                "children": [
                                                    {
                                                        "name": "Skithos",
                                                        "id": "118",
                                                        "sire": "117"
                                                    },
                                                    {
                                                        "name": "Robert Kross",
                                                        "id": "119",
                                                        "sire": "117",
                                                        "children": [
                                                            {
                                                                "name": "Juan-Miguel Ramirez",
                                                                "id": "120",
                                                                "sire": "119"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Örményországi Helena",
                                                "id": "121",
                                                "sire": "97",
                                                "children": [
                                                    {
                                                        "name": "Örmény Ventruek",
                                                        "id": "122",
                                                        "sire": "121"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Septima Dominica",
                                        "id": "123",
                                        "sire": "90",
                                        "children": [
                                            {
                                                "name": "Nicepherus",
                                                "id": "124",
                                                "sire": "123",
                                                "children": [
                                                    {
                                                        "name": "Theodora",
                                                        "id": "125",
                                                        "sire": "124",
                                                        "children": [
                                                            {
                                                                "name": "Thesszaloniki Basil",
                                                                "id": "126",
                                                                "sire": "125",
                                                                "children": [
                                                                    {
                                                                        "name": "Balkáni Ventruek",
                                                                        "id": "127",
                                                                        "sire": "126"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Orosz Ventruek",
                                                        "id": "128",
                                                        "sire": "124"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Ducas",
                                                "id": "129",
                                                "sire": "123",
                                                "children": [
                                                    {
                                                        "name": "Anna Comnena",
                                                        "id": "130",
                                                        "sire": "129",
                                                        "children": [
                                                            {
                                                                "name": "Irene Stellas",
                                                                "id": "131",
                                                                "sire": "130",
                                                                "children": [
                                                                    {
                                                                        "name": "Damiano Alvizio",
                                                                        "id": "132",
                                                                        "sire": "131"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Hardestadt az Öreg",
                                        "id": "133",
                                        "sire": "90",
                                        "children": [
                                            {
                                                "name": "Jürgen von Verden",
                                                "id": "134",
                                                "sire": "133"
                                            },
                                            {
                                                "name": "Heinz Eulau",
                                                "id": "135",
                                                "sire": "133"
                                            },
                                            {
                                                "name": "Frazier",
                                                "id": "136",
                                                "sire": "133",
                                                "children": [
                                                    {
                                                        "name": "Wittmann Antall",
                                                        "id": "137",
                                                        "sire": "136"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Hardestadt az Ifjú",
                                                "id": "138",
                                                "sire": "133",
                                                "children": [
                                                    {
                                                        "name": "Jan Pieterzoon",
                                                        "id": "139",
                                                        "sire": "138"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Alexander",
                                "id": "140",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Demetrius",
                                        "id": "141",
                                        "sire": "140",
                                        "children": [
                                            {
                                                "name": "Rhiothamus",
                                                "id": "142",
                                                "sire": "141",
                                                "children": [
                                                    {
                                                        "name": "Charlemagne",
                                                        "id": "143",
                                                        "sire": "142",
                                                        "children": [
                                                            {
                                                                "name": "Benedict",
                                                                "id": "144",
                                                                "sire": "143"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Justania",
                                                "id": "145",
                                                "sire": "141",
                                                "children": [
                                                    {
                                                        "name": "Gilbert d'Harfleur",
                                                        "id": "146",
                                                        "sire": "145"
                                                    },
                                                    {
                                                        "name": "Anya Krylova",
                                                        "id": "147",
                                                        "sire": "145",
                                                        "children": [
                                                            {
                                                                "name": "Nikolai",
                                                                "id": "148",
                                                                "sire": "147",
                                                                "children": [
                                                                    {
                                                                        "name": "Piotr",
                                                                        "id": "149",
                                                                        "sire": "148",
                                                                        "children": [
                                                                            {
                                                                                "name": "Lengyel Ventruek",
                                                                                "id": "150",
                                                                                "sire": "149"
                                                                            },
                                                                            {
                                                                                "name": "Moszkvai Seinia",
                                                                                "id": "151",
                                                                                "sire": "149"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Balti Ventruek",
                                                                "id": "152",
                                                                "sire": "147"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Victoria Sinclair",
                                                        "id": "153",
                                                        "sire": "145"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Eleanor d'Harcour",
                                                "id": "154",
                                                "sire": "141",
                                                "children": [
                                                    {
                                                        "name": "Norman Ventruek",
                                                        "id": "155",
                                                        "sire": "154"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Gaius Marcellus",
                                        "id": "156",
                                        "sire": "140",
                                        "children": [
                                            {
                                                "name": "Doran",
                                                "id": "157",
                                                "sire": "156",
                                                "children": [
                                                    {
                                                        "name": "Philippe de Margaux",
                                                        "id": "158",
                                                        "sire": "157",
                                                        "children": [
                                                            {
                                                                "name": "Enguerrand",
                                                                "id": "159",
                                                                "sire": "158"
                                                            },
                                                            {
                                                                "name": "Ogier Fouinon",
                                                                "id": "160",
                                                                "sire": "158",
                                                                "children": [
                                                                    {
                                                                        "name": "Marcelle Danlen",
                                                                        "id": "161",
                                                                        "sire": "160",
                                                                        "children": [
                                                                            {
                                                                                "name": "Yvonne",
                                                                                "id": "162",
                                                                                "sire": "161",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Louis Fortier",
                                                                                        "id": "163",
                                                                                        "sire": "162",
                                                                                        "children": [
                                                                                            {
                                                                                                "name": "Miroslava Nikolajevna Silina",
                                                                                                "id": "164",
                                                                                                "sire": "163"
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Tiberius",
                                        "id": "165",
                                        "sire": "140",
                                        "children": [
                                            {
                                                "name": "Aquitániai Odo",
                                                "id": "166",
                                                "sire": "165",
                                                "children": [
                                                    {
                                                        "name": "York-i Margit",
                                                        "id": "167",
                                                        "sire": "166"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Saviarre grófn",
                                                "id": "168",
                                                "sire": "165"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Geoffri du Temple",
                                        "id": "169",
                                        "sire": "140",
                                        "children": [
                                            {
                                                "name": "Bruce de Guy",
                                                "id": "170",
                                                "sire": "169",
                                                "children": [
                                                    {
                                                        "name": "Kanadai Ventruek",
                                                        "id": "171",
                                                        "sire": "170"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Mithras",
                                "id": "172",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Indiai Ventruek",
                                        "id": "173",
                                        "sire": "172"
                                    },
                                    {
                                        "name": "Perzsa Ventruek",
                                        "id": "174",
                                        "sire": "172"
                                    },
                                    {
                                        "name": "Del'Roh",
                                        "id": "175",
                                        "sire": "172",
                                        "children": [
                                            {
                                                "name": "Mezopotámiai Ventruek",
                                                "id": "176",
                                                "sire": "175"
                                            },
                                            {
                                                "name": "Bindusara",
                                                "id": "177",
                                                "sire": "175",
                                                "children": [
                                                    {
                                                        "name": "Charanna",
                                                        "id": "178",
                                                        "sire": "177",
                                                        "children": [
                                                            {
                                                                "name": "Narhari Virusha",
                                                                "id": "179",
                                                                "sire": "178"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Caius Marius",
                                                        "id": "180",
                                                        "sire": "177",
                                                        "children": [
                                                            {
                                                                "name": "Hrothulf",
                                                                "id": "181",
                                                                "sire": "180",
                                                                "children": [
                                                                    {
                                                                        "name": "Chiclena",
                                                                        "id": "182",
                                                                        "sire": "181"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Gracis Nostinus",
                                                                "id": "183",
                                                                "sire": "180"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Valerius",
                                                        "id": "184",
                                                        "sire": "177",
                                                        "children": [
                                                            {
                                                                "name": "Anne Bowsley",
                                                                "id": "185",
                                                                "sire": "184"
                                                            },
                                                            {
                                                                "name": "Cyril Masters",
                                                                "id": "186",
                                                                "sire": "184"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Marcellus Cicero",
                                                        "id": "187",
                                                        "sire": "177"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Qadi Vardek",
                                                "id": "188",
                                                "sire": "175",
                                                "children": [
                                                    {
                                                        "name": "Levantei Ventruek",
                                                        "id": "189",
                                                        "sire": "188"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Marcus",
                                                "id": "190",
                                                "sire": "175",
                                                "children": [
                                                    {
                                                        "name": "Stephen von Dorn",
                                                        "id": "191",
                                                        "sire": "190"
                                                    },
                                                    {
                                                        "name": "Joseph Bar",
                                                        "id": "192",
                                                        "sire": "190"
                                                    },
                                                    {
                                                        "name": "Arthur Logan",
                                                        "id": "193",
                                                        "sire": "190"
                                                    },
                                                    {
                                                        "name": "Lord Kelvin",
                                                        "id": "194",
                                                        "sire": "190",
                                                        "children": [
                                                            {
                                                                "name": "Victor James Rotschield",
                                                                "id": "195",
                                                                "sire": "194"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Robert Pedder",
                                                        "id": "196",
                                                        "sire": "190",
                                                        "children": [
                                                            {
                                                                "name": "Yong-Sung Chang",
                                                                "id": "197",
                                                                "sire": "196",
                                                                "children": [
                                                                    {
                                                                        "name": "Hong Kong-i Ventruek",
                                                                        "id": "198",
                                                                        "sire": "197"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Sennicherib",
                                        "id": "199",
                                        "sire": "172",
                                        "children": [
                                            {
                                                "name": "Tiglah-Adad",
                                                "id": "200",
                                                "sire": "199",
                                                "children": [
                                                    {
                                                        "name": "Asszír Ventruek",
                                                        "id": "201",
                                                        "sire": "200"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Cyras Artraxis",
                                                "id": "202",
                                                "sire": "199",
                                                "children": [
                                                    {
                                                        "name": "Nicephrous Baalikratonis",
                                                        "id": "203",
                                                        "sire": "202"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Celdric",
                                        "id": "204",
                                        "sire": "172",
                                        "children": [
                                            {
                                                "name": "Owain ap Ieuan",
                                                "id": "205",
                                                "sire": "204"
                                            },
                                            {
                                                "name": "Lucian Stewart",
                                                "id": "206",
                                                "sire": "204"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Hosszúfogú Sven",
                                        "id": "207",
                                        "sire": "172",
                                        "children": [
                                            {
                                                "name": "Gustav Mallenhous",
                                                "id": "208",
                                                "sire": "207"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Gomerland",
                                "id": "209",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Volstag-i Heinrich",
                                        "id": "210",
                                        "sire": "209",
                                        "children": [
                                            {
                                                "name": "Marcus Atilius Regulus",
                                                "id": "211",
                                                "sire": "210",
                                                "children": [
                                                    {
                                                        "name": "Siegfried",
                                                        "id": "212",
                                                        "sire": "211"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Árpádházi Bulcsú",
                                                "id": "213",
                                                "sire": "210",
                                                "children": [
                                                    {
                                                        "name": "Árpádházi Géza",
                                                        "id": "214",
                                                        "sire": "213",
                                                        "children": [
                                                            {
                                                                "name": "Orseolo Levente",
                                                                "id": "215",
                                                                "sire": "214",
                                                                "children": [
                                                                    {
                                                                        "name": "Szilágyi Mihály",
                                                                        "id": "216",
                                                                        "sire": "215",
                                                                        "children": [
                                                                            {
                                                                                "name": "báró Pálffy Balázs",
                                                                                "id": "217",
                                                                                "sire": "216"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "gróf Pálffy Aurél Zoltán",
                                                                        "id": "218",
                                                                        "sire": "215",
                                                                        "children": [
                                                                            {
                                                                                "name": "Sebessy Katalin",
                                                                                "id": "219",
                                                                                "sire": "218"
                                                                            },
                                                                            {
                                                                                "name": "Dr. Robert Kenton",
                                                                                "id": "220",
                                                                                "sire": "218"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Áprádházi Gizella",
                                                        "id": "221",
                                                        "sire": "213",
                                                        "children": [
                                                            {
                                                                "name": "Váry Eld (Gustavus)",
                                                                "id": "222",
                                                                "sire": "221",
                                                                "children": [
                                                                    {
                                                                        "name": "Váry Alexander",
                                                                        "id": "223",
                                                                        "sire": "222"
                                                                    },
                                                                    {
                                                                        "name": "gróf Batthyány Ilona",
                                                                        "id": "224",
                                                                        "sire": "222",
                                                                        "children": [
                                                                            {
                                                                                "name": "báró Erddy János",
                                                                                "id": "225",
                                                                                "sire": "224"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Vencel Rikard",
                                                        "id": "226",
                                                        "sire": "213"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Bohémiai Jadviga Almanov",
                                                "id": "227",
                                                "sire": "210",
                                                "children": [
                                                    {
                                                        "name": "báró Jan Hredel",
                                                        "id": "228",
                                                        "sire": "227",
                                                        "children": [
                                                            {
                                                                "name": "gróf Rudolf Brandl",
                                                                "id": "229",
                                                                "sire": "228",
                                                                "children": [
                                                                    {
                                                                        "name": "Cseh Ventruek",
                                                                        "id": "230",
                                                                        "sire": "229"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Ladek Visnitz",
                                                        "id": "231",
                                                        "sire": "227",
                                                        "children": [
                                                            {
                                                                "name": "Alexandr Sreik",
                                                                "id": "232",
                                                                "sire": "231",
                                                                "children": [
                                                                    {
                                                                        "name": "Késmárky Zsófia",
                                                                        "id": "233",
                                                                        "sire": "232"
                                                                    },
                                                                    {
                                                                        "name": "Hanna Marek",
                                                                        "id": "234",
                                                                        "sire": "232"
                                                                    },
                                                                    {
                                                                        "name": "Lukas Ziman",
                                                                        "id": "235",
                                                                        "sire": "232"
                                                                    },
                                                                    {
                                                                        "name": "Emilia Clark",
                                                                        "id": "236",
                                                                        "sire": "232"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Árpádházi II. András",
                                                "id": "237",
                                                "sire": "210",
                                                "children": [
                                                    {
                                                        "name": "gróf Mailáth Erzsébet",
                                                        "id": "238",
                                                        "sire": "237",
                                                        "children": [
                                                            {
                                                                "name": "gróf Mailáth Gergely",
                                                                "id": "239",
                                                                "sire": "238",
                                                                "children": [
                                                                    {
                                                                        "name": "gróf Pallavichini Endre",
                                                                        "id": "240",
                                                                        "sire": "239",
                                                                        "children": [
                                                                            {
                                                                                "name": "gróf Pallavichini Péter Ödön",
                                                                                "id": "241",
                                                                                "sire": "240"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "gróf Eszterházy Polyxéna",
                                                                        "id": "242",
                                                                        "sire": "239"
                                                                    },
                                                                    {
                                                                        "name": "gróf Teleki Alíz",
                                                                        "id": "243",
                                                                        "sire": "239"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "gróf Mailáth Erzsébet Anna",
                                                                "id": "244",
                                                                "sire": "238",
                                                                "children": [
                                                                    {
                                                                        "name": "báró Jaksich Gábor",
                                                                        "id": "245",
                                                                        "sire": "244",
                                                                        "children": [
                                                                            {
                                                                                "name": "gróf Perényi János",
                                                                                "id": "246",
                                                                                "sire": "245"
                                                                            },
                                                                            {
                                                                                "name": "Péterffy Viktor",
                                                                                "id": "247",
                                                                                "sire": "245"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Zalay Mihály",
                                                        "id": "248",
                                                        "sire": "237",
                                                        "children": [
                                                            {
                                                                "name": "gróf Grecsey Jen",
                                                                "id": "249",
                                                                "sire": "248"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Szebeni Miklós",
                                                        "id": "250",
                                                        "sire": "237",
                                                        "children": [
                                                            {
                                                                "name": "Istvánffy Márton",
                                                                "id": "251",
                                                                "sire": "250"
                                                            },
                                                            {
                                                                "name": "gróf Nádasdy László",
                                                                "id": "252",
                                                                "sire": "250",
                                                                "children": [
                                                                    {
                                                                        "name": "Izabella",
                                                                        "id": "253",
                                                                        "sire": "252"
                                                                    },
                                                                    {
                                                                        "name": "Klauzál Gábor",
                                                                        "id": "254",
                                                                        "sire": "252",
                                                                        "children": [
                                                                            {
                                                                                "name": "vitéz Csabay Károly",
                                                                                "id": "255",
                                                                                "sire": "254"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "Solymossy Eliza",
                                                                        "id": "256",
                                                                        "sire": "252"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Spanyol és Latin-Amerika-i Ventruek",
                                        "id": "257",
                                        "sire": "209"
                                    }
                                ]
                            },
                            {
                                "name": "Erik Eigermann",
                                "id": "258",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Fabrizio Ulfia",
                                        "id": "259",
                                        "sire": "258",
                                        "children": [
                                            {
                                                "name": "Szentszéki Ventruek",
                                                "id": "260",
                                                "sire": "259"
                                            },
                                            {
                                                "name": "Baylor",
                                                "id": "261",
                                                "sire": "259",
                                                "children": [
                                                    {
                                                        "name": "Eleanor Hodge",
                                                        "id": "262",
                                                        "sire": "261",
                                                        "children": [
                                                            {
                                                                "name": "Benjamin",
                                                                "id": "263",
                                                                "sire": "262"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "dr. Joshua McCallister",
                                                        "id": "264",
                                                        "sire": "261"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Ilse Reinegger",
                                        "id": "265",
                                        "sire": "258",
                                        "children": [
                                            {
                                                "name": "Gustav Bredenstein",
                                                "id": "266",
                                                "sire": "265",
                                                "children": [
                                                    {
                                                        "name": "Wilhelm Waldburg",
                                                        "id": "267",
                                                        "sire": "266",
                                                        "children": [
                                                            {
                                                                "name": "Henriette",
                                                                "id": "268",
                                                                "sire": "267"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Katarina Kornfeld",
                                                        "id": "269",
                                                        "sire": "266"
                                                    },
                                                    {
                                                        "name": "Köln-i Frigyes",
                                                        "id": "270",
                                                        "sire": "266"
                                                    },
                                                    {
                                                        "name": "Peter Kleist",
                                                        "id": "271",
                                                        "sire": "266"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Maltheas",
                                "id": "272",
                                "sire": "3",
                                "children": [
                                    {
                                        "name": "Balthazar",
                                        "id": "273",
                                        "sire": "272",
                                        "children": [
                                            {
                                                "name": "Ea Adapa",
                                                "id": "274",
                                                "sire": "273"
                                            },
                                            {
                                                "name": "Anushin-Rawan",
                                                "id": "275",
                                                "sire": "273"
                                            },
                                            {
                                                "name": "Gregoria Rowlands",
                                                "id": "276",
                                                "sire": "273",
                                                "children": [
                                                    {
                                                        "name": "Upton Rowlands",
                                                        "id": "277",
                                                        "sire": "276"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Rashur",
                                        "id": "278",
                                        "sire": "272",
                                        "children": [
                                            {
                                                "name": "Nicholas",
                                                "id": "279",
                                                "sire": "278",
                                                "children": [
                                                    {
                                                        "name": "Abram",
                                                        "id": "280",
                                                        "sire": "279",
                                                        "children": [
                                                            {
                                                                "name": "Tennant Usher",
                                                                "id": "281",
                                                                "sire": "280",
                                                                "children": [
                                                                    {
                                                                        "name": "Ausztráliai Ventruek",
                                                                        "id": "282",
                                                                        "sire": "281"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Datura",
                                                "id": "283",
                                                "sire": "278",
                                                "children": [
                                                    {
                                                        "name": "Mexikói Ventruek",
                                                        "id": "284",
                                                        "sire": "283"
                                                    },
                                                    {
                                                        "name": "Mahmúd",
                                                        "id": "285",
                                                        "sire": "283",
                                                        "children": [
                                                            {
                                                                "name": "El-Nisri",
                                                                "id": "286",
                                                                "sire": "285",
                                                                "children": [
                                                                    {
                                                                        "name": "Mohammad Hossein Mirza",
                                                                        "id": "287",
                                                                        "sire": "286"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Lodin",
                                                        "id": "288",
                                                        "sire": "283",
                                                        "children": [
                                                            {
                                                                "name": "Sir Walter Nash",
                                                                "id": "289",
                                                                "sire": "288"
                                                            },
                                                            {
                                                                "name": "Horatio Ballard",
                                                                "id": "290",
                                                                "sire": "288",
                                                                "children": [
                                                                    {
                                                                        "name": "Alan Sovereign",
                                                                        "id": "291",
                                                                        "sire": "290"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "Saulot / Zao-lat",
                        "id": "292",
                        "sire": "2",
                        "children": [
                            {
                                "name": "Rayzeel",
                                "id": "293",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Myrael",
                                        "id": "294",
                                        "sire": "293",
                                        "children": [
                                            {
                                                "name": "Genevieve",
                                                "id": "295",
                                                "sire": "294",
                                                "children": [
                                                    {
                                                        "name": "Wenceslaus",
                                                        "id": "296",
                                                        "sire": "295",
                                                        "children": [
                                                            {
                                                                "name": "Pazia",
                                                                "id": "297",
                                                                "sire": "296",
                                                                "children": [
                                                                    {
                                                                        "name": "Bizánci Salubrik",
                                                                        "id": "298",
                                                                        "sire": "297"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Nabur-Het",
                                                "id": "299",
                                                "sire": "294",
                                                "children": [
                                                    {
                                                        "name": "Kydos",
                                                        "id": "300",
                                                        "sire": "299",
                                                        "children": [
                                                            {
                                                                "name": "Neberoth",
                                                                "id": "301",
                                                                "sire": "300",
                                                                "children": [
                                                                    {
                                                                        "name": "Adonai",
                                                                        "id": "302",
                                                                        "sire": "301",
                                                                        "children": [
                                                                            {
                                                                                "name": "Énekes vérvonal / Sabbatista Salubrik",
                                                                                "id": "303",
                                                                                "sire": "302"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Samiel",
                                "id": "304",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Ithuriel",
                                        "id": "305",
                                        "sire": "304",
                                        "children": [
                                            {
                                                "name": "Hilel",
                                                "id": "306",
                                                "sire": "305",
                                                "children": [
                                                    {
                                                        "name": "Gabriel",
                                                        "id": "307",
                                                        "sire": "306",
                                                        "children": [
                                                            {
                                                                "name": "Philipus-i Althea",
                                                                "id": "308",
                                                                "sire": "307",
                                                                "children": [
                                                                    {
                                                                        "name": "Yael",
                                                                        "id": "309",
                                                                        "sire": "308",
                                                                        "children": [
                                                                            {
                                                                                "name": "Thomas",
                                                                                "id": "310",
                                                                                "sire": "309",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Kervos",
                                                                                        "id": "311",
                                                                                        "sire": "310"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Silas",
                                                                "id": "312",
                                                                "sire": "307",
                                                                "children": [
                                                                    {
                                                                        "name": "Levantei Salubrik",
                                                                        "id": "313",
                                                                        "sire": "312"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Aariel",
                                        "id": "314",
                                        "sire": "304",
                                        "children": [
                                            {
                                                "name": "Dokiel",
                                                "id": "315",
                                                "sire": "314",
                                                "children": [
                                                    {
                                                        "name": "Kadiel",
                                                        "id": "316",
                                                        "sire": "315",
                                                        "children": [
                                                            {
                                                                "name": "Esharel",
                                                                "id": "317",
                                                                "sire": "316",
                                                                "children": [
                                                                    {
                                                                        "name": "Bahjat",
                                                                        "id": "318",
                                                                        "sire": "317",
                                                                        "children": [
                                                                            {
                                                                                "name": "Indiai Salubrik",
                                                                                "id": "319",
                                                                                "sire": "318"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Uriel",
                                        "id": "320",
                                        "sire": "304",
                                        "children": [
                                            {
                                                "name": "Azrael",
                                                "id": "321",
                                                "sire": "320",
                                                "children": [
                                                    {
                                                        "name": "Római Salubrik",
                                                        "id": "322",
                                                        "sire": "321"
                                                    },
                                                    {
                                                        "name": "Spanyol Salubrik",
                                                        "id": "323",
                                                        "sire": "321"
                                                    },
                                                    {
                                                        "name": "Francia Salubrik",
                                                        "id": "324",
                                                        "sire": "321"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Ezrael",
                                        "id": "325",
                                        "sire": "304",
                                        "children": [
                                            {
                                                "name": "Baradiel",
                                                "id": "326",
                                                "sire": "325",
                                                "children": [
                                                    {
                                                        "name": "Scatha",
                                                        "id": "327",
                                                        "sire": "326",
                                                        "children": [
                                                            {
                                                                "name": "Keresztes Salubrik",
                                                                "id": "328",
                                                                "sire": "327"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Za'aphiel",
                                        "id": "329",
                                        "sire": "304",
                                        "children": [
                                            {
                                                "name": "Karthágói Salubrik",
                                                "id": "330",
                                                "sire": "329"
                                            },
                                            {
                                                "name": "Egyiptomi Salubrik",
                                                "id": "331",
                                                "sire": "329"
                                            },
                                            {
                                                "name": "Afrikai Salubrik(Nkolo Zao)",
                                                "id": "332",
                                                "sire": "329"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Yakov",
                                "id": "333",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Karesh",
                                        "id": "334",
                                        "sire": "333"
                                    },
                                    {
                                        "name": "Javaniel",
                                        "id": "335",
                                        "sire": "333",
                                        "children": [
                                            {
                                                "name": "Orpheus",
                                                "id": "336",
                                                "sire": "335",
                                                "children": [
                                                    {
                                                        "name": "Achmet, az Álmodó",
                                                        "id": "337",
                                                        "sire": "336",
                                                        "children": [
                                                            {
                                                                "name": "Aisha bint Wahiba",
                                                                "id": "338",
                                                                "sire": "337",
                                                                "children": [
                                                                    {
                                                                        "name": "Arab Salubrik",
                                                                        "id": "339",
                                                                        "sire": "338"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Török Salubrik (Látnok vérvonal)",
                                                                "id": "340",
                                                                "sire": "337"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Hrorsh",
                                "id": "341",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Vekis",
                                        "id": "342",
                                        "sire": "341",
                                        "children": [
                                            {
                                                "name": "Ahab, az Áruló",
                                                "id": "343",
                                                "sire": "342"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Simeon",
                                        "id": "344",
                                        "sire": "341",
                                        "children": [
                                            {
                                                "name": "Generys",
                                                "id": "345",
                                                "sire": "344",
                                                "children": [
                                                    {
                                                        "name": "Hershel",
                                                        "id": "346",
                                                        "sire": "345",
                                                        "children": [
                                                            {
                                                                "name": "Német Salubrik",
                                                                "id": "347",
                                                                "sire": "346"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Matthias",
                                                        "id": "348",
                                                        "sire": "345",
                                                        "children": [
                                                            {
                                                                "name": "Marius",
                                                                "id": "349",
                                                                "sire": "348",
                                                                "children": [
                                                                    {
                                                                        "name": "Angol Salubrik",
                                                                        "id": "350",
                                                                        "sire": "349"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Nergal / Shaitan / Adriel / Huitzilopochtli",
                                "id": "351",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Cybele",
                                        "id": "352",
                                        "sire": "351",
                                        "children": [
                                            {
                                                "name": "Mytale / Petaniqua",
                                                "id": "353",
                                                "sire": "352"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Yeremiah",
                                        "id": "354",
                                        "sire": "351",
                                        "children": [
                                            {
                                                "name": "Nidon, a Vak",
                                                "id": "355",
                                                "sire": "354",
                                                "children": [
                                                    {
                                                        "name": "Azanael",
                                                        "id": "356",
                                                        "sire": "355",
                                                        "children": [
                                                            {
                                                                "name": "Al-Harim",
                                                                "id": "357",
                                                                "sire": "356",
                                                                "children": [
                                                                    {
                                                                        "name": "Ansen",
                                                                        "id": "358",
                                                                        "sire": "357"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Camazotz / Nezahualcoyotl",
                                        "id": "359",
                                        "sire": "351",
                                        "children": [
                                            {
                                                "name": "Hortator / Tlazolteotl",
                                                "id": "360",
                                                "sire": "359",
                                                "children": [
                                                    {
                                                        "name": "Delfoso",
                                                        "id": "361",
                                                        "sire": "360",
                                                        "children": [
                                                            {
                                                                "name": "Don Benedict",
                                                                "id": "362",
                                                                "sire": "361"
                                                            },
                                                            {
                                                                "name": "Domingo",
                                                                "id": "363",
                                                                "sire": "361"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Azték Baalik",
                                                        "id": "364",
                                                        "sire": "360"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Moloch",
                                "id": "365",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Annazir",
                                        "id": "366",
                                        "sire": "365",
                                        "children": [
                                            {
                                                "name": "Anaduk",
                                                "id": "367",
                                                "sire": "366",
                                                "children": [
                                                    {
                                                        "name": "Ma-Ri-Ah / Fekete Mária",
                                                        "id": "368",
                                                        "sire": "367"
                                                    },
                                                    {
                                                        "name": "K'thstl",
                                                        "id": "369",
                                                        "sire": "367",
                                                        "children": [
                                                            {
                                                                "name": "Sargon",
                                                                "id": "370",
                                                                "sire": "369"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Darak",
                                                        "id": "371",
                                                        "sire": "367"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Antonio de Figo",
                                                "id": "372",
                                                "sire": "366",
                                                "children": [
                                                    {
                                                        "name": "Giotto Verducci",
                                                        "id": "373",
                                                        "sire": "372"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Seker, a Vörös Halál",
                                "id": "374",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "A Rettent Éj Els Gyermeke",
                                        "id": "375",
                                        "sire": "374"
                                    },
                                    {
                                        "name": "A Rettent Éj Második Gyermeke",
                                        "id": "376",
                                        "sire": "374"
                                    },
                                    {
                                        "name": "A Rettent Éj Harmadik Gyermeke",
                                        "id": "377",
                                        "sire": "374"
                                    }
                                ]
                            },
                            {
                                "name": "Zao-zei",
                                "id": "378",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Az Árva Tolvajok",
                                        "id": "379",
                                        "sire": "378"
                                    }
                                ]
                            },
                            {
                                "name": "Zao-xue",
                                "id": "380",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Az Árva Tudósok",
                                        "id": "381",
                                        "sire": "380"
                                    }
                                ]
                            },
                            {
                                "name": "Akhraziel",
                                "id": "382",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Madiel",
                                        "id": "383",
                                        "sire": "382"
                                    },
                                    {
                                        "name": "Nuriel",
                                        "id": "384",
                                        "sire": "382",
                                        "children": [
                                            {
                                                "name": "Oreniel al-Noor",
                                                "id": "385",
                                                "sire": "384",
                                                "children": [
                                                    {
                                                        "name": "Amphiloctes",
                                                        "id": "386",
                                                        "sire": "385",
                                                        "children": [
                                                            {
                                                                "name": "Görög Salubrik",
                                                                "id": "387",
                                                                "sire": "386"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Gennadios",
                                                        "id": "388",
                                                        "sire": "385",
                                                        "children": [
                                                            {
                                                                "name": "Perzsa Salubrik",
                                                                "id": "389",
                                                                "sire": "388"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Nahum ben Enosh",
                                "id": "390",
                                "sire": "292",
                                "children": [
                                    {
                                        "name": "Israel",
                                        "id": "391",
                                        "sire": "390",
                                        "children": [
                                            {
                                                "name": "Nathaniel",
                                                "id": "392",
                                                "sire": "391",
                                                "children": [
                                                    {
                                                        "name": "Kánaánita Salubrik",
                                                        "id": "393",
                                                        "sire": "392"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "Ashur, a Kappadókiai",
                        "id": "394",
                        "sire": "2",
                        "children": [
                            {
                                "name": "Caias",
                                "id": "395",
                                "sire": "394",
                                "children": [
                                    {
                                        "name": "Egyiptomi Kappadókok",
                                        "id": "396",
                                        "sire": "395"
                                    }
                                ]
                            },
                            {
                                "name": "Japeth / A Kapucínus",
                                "id": "397",
                                "sire": "394",
                                "children": [
                                    {
                                        "name": "Constancia / Unre",
                                        "id": "398",
                                        "sire": "397",
                                        "children": [
                                            {
                                                "name": "Mekharel",
                                                "id": "399",
                                                "sire": "398",
                                                "children": [
                                                    {
                                                        "name": "Egothia",
                                                        "id": "400",
                                                        "sire": "399",
                                                        "children": [
                                                            {
                                                                "name": "Agaitas",
                                                                "id": "401",
                                                                "sire": "400",
                                                                "children": [
                                                                    {
                                                                        "name": "Kis-Ázsiai Kappadókok",
                                                                        "id": "402",
                                                                        "sire": "401"
                                                                    },
                                                                    {
                                                                        "name": "Római Kappadókok",
                                                                        "id": "403",
                                                                        "sire": "401"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Anisa Marianna Lopez",
                                                                "id": "404",
                                                                "sire": "400",
                                                                "children": [
                                                                    {
                                                                        "name": "Spanyol Kappadókok",
                                                                        "id": "405",
                                                                        "sire": "404"
                                                                    },
                                                                    {
                                                                        "name": "Német Kappadókok",
                                                                        "id": "406",
                                                                        "sire": "404"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Ambrogio Giovanni",
                                                "id": "407",
                                                "sire": "398",
                                                "children": [
                                                    {
                                                        "name": "Gillespi Giovanni",
                                                        "id": "408",
                                                        "sire": "407"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Abraham",
                                        "id": "409",
                                        "sire": "397",
                                        "children": [
                                            {
                                                "name": "Theophilis",
                                                "id": "410",
                                                "sire": "409",
                                                "children": [
                                                    {
                                                        "name": "Görög Kappadókok",
                                                        "id": "411",
                                                        "sire": "410"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Adam",
                                                "id": "412",
                                                "sire": "409",
                                                "children": [
                                                    {
                                                        "name": "Levantei Kappadókok",
                                                        "id": "413",
                                                        "sire": "412"
                                                    },
                                                    {
                                                        "name": "Afrikai Kappadókok (Mla Watu)",
                                                        "id": "414",
                                                        "sire": "412"
                                                    },
                                                    {
                                                        "name": "Malakiah",
                                                        "id": "415",
                                                        "sire": "412",
                                                        "children": [
                                                            {
                                                                "name": "Jervais testvér",
                                                                "id": "416",
                                                                "sire": "415",
                                                                "children": [
                                                                    {
                                                                        "name": "Garinol",
                                                                        "id": "417",
                                                                        "sire": "416",
                                                                        "children": [
                                                                            {
                                                                                "name": "Serena",
                                                                                "id": "418",
                                                                                "sire": "417",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Cseh Kappadókok",
                                                                                        "id": "419",
                                                                                        "sire": "418"
                                                                                    }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "name": " Mercurio",
                                                                                "id": "420",
                                                                                "sire": "417"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Lord Camden",
                                        "id": "421",
                                        "sire": "397",
                                        "children": [
                                            {
                                                "name": "Maria Asuncion",
                                                "id": "422",
                                                "sire": "421",
                                                "children": [
                                                    {
                                                        "name": "Francia Kappadókok",
                                                        "id": "423",
                                                        "sire": "422"
                                                    },
                                                    {
                                                        "name": "Angol Kappadókok",
                                                        "id": "424",
                                                        "sire": "422"
                                                    },
                                                    {
                                                        "name": "Karl Gregorj Pranek / Orpheus",
                                                        "id": "425",
                                                        "sire": "422"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Lazarus",
                                "id": "426",
                                "sire": "394",
                                "children": [
                                    {
                                        "name": "Lahmia",
                                        "id": "427",
                                        "sire": "426",
                                        "children": [
                                            {
                                                "name": "Lahmiák",
                                                "id": "428",
                                                "sire": "427"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Troglodytia",
                                        "id": "429",
                                        "sire": "426"
                                    },
                                    {
                                        "name": "Samedi Báró",
                                        "id": "430",
                                        "sire": "426",
                                        "children": [
                                            {
                                                "name": "Morlock",
                                                "id": "431",
                                                "sire": "430",
                                                "children": [
                                                    {
                                                        "name": "Baroque",
                                                        "id": "432",
                                                        "sire": "431",
                                                        "children": [
                                                            {
                                                                "name": "Karibi Samedik",
                                                                "id": "433",
                                                                "sire": "432"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Genina",
                                                "id": "434",
                                                "sire": "430"
                                            },
                                            {
                                                "name": "Jorge de la Muerte",
                                                "id": "435",
                                                "sire": "430",
                                                "children": [
                                                    {
                                                        "name": "Macoute",
                                                        "id": "436",
                                                        "sire": "435",
                                                        "children": [
                                                            {
                                                                "name": "Brigitte",
                                                                "id": "437",
                                                                "sire": "436",
                                                                "children": [
                                                                    {
                                                                        "name": "Mexikói Samedik",
                                                                        "id": "438",
                                                                        "sire": "437"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Reg Driscoll",
                                                "id": "439",
                                                "sire": "430",
                                                "children": [
                                                    {
                                                        "name": "Amerikai Samedik",
                                                        "id": "440",
                                                        "sire": "439"
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Jack Dawson",
                                                "id": "441",
                                                "sire": "430",
                                                "children": [
                                                    {
                                                        "name": "Vanda le Claire",
                                                        "id": "442",
                                                        "sire": "441",
                                                        "children": [
                                                            {
                                                                "name": "George Frederick",
                                                                "id": "443",
                                                                "sire": "442",
                                                                "children": [
                                                                    {
                                                                        "name": "Lithrac",
                                                                        "id": "444",
                                                                        "sire": "443"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Lameth, a Sötét Megváltó",
                                "id": "445",
                                "sire": "394"
                            },
                            {
                                "name": "Byzar / Mahatma",
                                "id": "446",
                                "sire": "394",
                                "children": [
                                    {
                                        "name": "Alexia Theusa",
                                        "id": "447",
                                        "sire": "446",
                                        "children": [
                                            {
                                                "name": "Bizánci Kappadókok",
                                                "id": "448",
                                                "sire": "447"
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Antiokhiai Kürosz",
                                        "id": "449",
                                        "sire": "446",
                                        "children": [
                                            {
                                                "name": "Nabateus Aretas",
                                                "id": "450",
                                                "sire": "449",
                                                "children": [
                                                    {
                                                        "name": "Gelias",
                                                        "id": "451",
                                                        "sire": "450",
                                                        "children": [
                                                            {
                                                                "name": "Khayrat",
                                                                "id": "452",
                                                                "sire": "451",
                                                                "children": [
                                                                    {
                                                                        "name": "Ishaq",
                                                                        "id": "453",
                                                                        "sire": "452",
                                                                        "children": [
                                                                            {
                                                                                "name": "Arab Kappadókok",
                                                                                "id": "454",
                                                                                "sire": "453"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Török Kappadókok",
                                                "id": "455",
                                                "sire": "449"
                                            },
                                            {
                                                "name": "Thrákiai Amália",
                                                "id": "456",
                                                "sire": "449",
                                                "children": [
                                                    {
                                                        "name": "Burgundiai Boderick",
                                                        "id": "457",
                                                        "sire": "456",
                                                        "children": [
                                                            {
                                                                "name": "Keresztes Kappadókok",
                                                                "id": "458",
                                                                "sire": "457"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "name": "Ungol",
                                        "id": "459",
                                        "sire": "446",
                                        "children": [
                                            {
                                                "name": "Orosz Kappadókok",
                                                "id": "460",
                                                "sire": "459"
                                            },
                                            {
                                                "name": "Kazimirez, a Néma",
                                                "id": "461",
                                                "sire": "459",
                                                "children": [
                                                    {
                                                        "name": "Lengyel Kappadókok",
                                                        "id": "462",
                                                        "sire": "461"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "name": "Augusto Giovanni",
                                "id": "463",
                                "sire": "394",
                                "children": [
                                    {
                                        "name": "Claudius Giovanni",
                                        "id": "464",
                                        "sire": "463",
                                        "children": [
                                            {
                                                "name": "Ignazo Giovanni",
                                                "id": "465",
                                                "sire": "464",
                                                "children": [
                                                    {
                                                        "name": "Lucretia Giovanni",
                                                        "id": "466",
                                                        "sire": "465",
                                                        "children": [
                                                            {
                                                                "name": "Giorgio Giovanni",
                                                                "id": "467",
                                                                "sire": "466",
                                                                "children": [
                                                                    {
                                                                        "name": "Carmina Giovanni",
                                                                        "id": "468",
                                                                        "sire": "467",
                                                                        "children": [
                                                                            {
                                                                                "name": "Rosario Giovanni",
                                                                                "id": "469",
                                                                                "sire": "468",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Salvatore Giovanni",
                                                                                        "id": "470",
                                                                                        "sire": "469"
                                                                                    }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "name": "Német Königek",
                                                                                "id": "471",
                                                                                "sire": "468"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "Genevra Giovanni",
                                                                        "id": "472",
                                                                        "sire": "467",
                                                                        "children": [
                                                                            {
                                                                                "name": "Jason Milliner",
                                                                                "id": "473",
                                                                                "sire": "472",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Francis Milliner",
                                                                                        "id": "474",
                                                                                        "sire": "473",
                                                                                        "children": [
                                                                                            {
                                                                                                "name": "Amerikai Millinerek",
                                                                                                "id": "475",
                                                                                                "sire": "474"
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Baldesar Rossellini",
                                                        "id": "476",
                                                        "sire": "465",
                                                        "children": [
                                                            {
                                                                "name": "Vance Rosellini",
                                                                "id": "477",
                                                                "sire": "476",
                                                                "children": [
                                                                    {
                                                                        "name": "Olasz Rosellinik",
                                                                        "id": "478",
                                                                        "sire": "477"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Rosaura Rosellini",
                                                                "id": "479",
                                                                "sire": "476",
                                                                "children": [
                                                                    {
                                                                        "name": "Matteo Rosellini",
                                                                        "id": "480",
                                                                        "sire": "479",
                                                                        "children": [
                                                                            {
                                                                                "name": "Patricia Rosellini",
                                                                                "id": "481",
                                                                                "sire": "480",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Giacomo Rosellini",
                                                                                        "id": "482",
                                                                                        "sire": "481",
                                                                                        "children": [
                                                                                            {
                                                                                                "name": "Riana Rosellini",
                                                                                                "id": "483",
                                                                                                "sire": "482",
                                                                                                "children": [
                                                                                                    {
                                                                                                        "name": "Alberto Rosellini",
                                                                                                        "id": "484",
                                                                                                        "sire": "483"
                                                                                                    }
                                                                                                ]
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Andreas Giovanni",
                                                "id": "485",
                                                "sire": "464",
                                                "children": [
                                                    {
                                                        "name": "Mario Giovanni",
                                                        "id": "486",
                                                        "sire": "485",
                                                        "children": [
                                                            {
                                                                "name": "Luisa Calabria",
                                                                "id": "487",
                                                                "sire": "486",
                                                                "children": [
                                                                    {
                                                                        "name": "Olasz Giovannik",
                                                                        "id": "488",
                                                                        "sire": "487"
                                                                    },
                                                                    {
                                                                        "name": "Latin-Amerikai Hidalgok",
                                                                        "id": "489",
                                                                        "sire": "487"
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "name": "Afrikai Ghibertik",
                                                                "id": "490",
                                                                "sire": "486"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Lisandro Giovanni",
                                                        "id": "491",
                                                        "sire": "485",
                                                        "children": [
                                                            {
                                                                "name": "Isabel Giovanni",
                                                                "id": "492",
                                                                "sire": "491"
                                                            },
                                                            {
                                                                "name": "Giancarlo Giovanni",
                                                                "id": "493",
                                                                "sire": "491",
                                                                "children": [
                                                                    {
                                                                        "name": "Enzo Giovanni",
                                                                        "id": "494",
                                                                        "sire": "493",
                                                                        "children": [
                                                                            {
                                                                                "name": "Valentino Eusebio Giovanni",
                                                                                "id": "495",
                                                                                "sire": "494"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Pietro Giovanni",
                                                "id": "496",
                                                "sire": "464",
                                                "children": [
                                                    {
                                                        "name": "Madeleine Giovanni",
                                                        "id": "497",
                                                        "sire": "496",
                                                        "children": [
                                                            {
                                                                "name": "Rafael Giovanni",
                                                                "id": "498",
                                                                "sire": "497",
                                                                "children": [
                                                                    {
                                                                        "name": "Francia Giovannik",
                                                                        "id": "499",
                                                                        "sire": "498"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "name": "Vincenzo Giovanni",
                                                        "id": "500",
                                                        "sire": "496",
                                                        "children": [
                                                            {
                                                                "name": "Francesco Giovanni",
                                                                "id": "501",
                                                                "sire": "500",
                                                                "children": [
                                                                    {
                                                                        "name": "Julietta Putanesca",
                                                                        "id": "502",
                                                                        "sire": "501",
                                                                        "children": [
                                                                            {
                                                                                "name": "Shlomo Rothstein",
                                                                                "id": "503",
                                                                                "sire": "502",
                                                                                "children": [
                                                                                    {
                                                                                        "name": "Amerikai Rothsteinek",
                                                                                        "id": "504",
                                                                                        "sire": "503"
                                                                                    }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "name": "Olasz Putanescák",
                                                                                "id": "505",
                                                                                "sire": "502"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "name": "Lupo Giovanni",
                                                                        "id": "506",
                                                                        "sire": "501",
                                                                        "children": [
                                                                            {
                                                                                "name": "Távol-Keleti Li Wengek",
                                                                                "id": "507",
                                                                                "sire": "506"
                                                                            },
                                                                            {
                                                                                "name": "Andreas Niccolo Giovanni",
                                                                                "id": "508",
                                                                                "sire": "506"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Giuseppe Giovanni",
                                                "id": "509",
                                                "sire": "464",
                                                "children": [
                                                    {
                                                        "name": "Markus Musa Giovanni",
                                                        "id": "510",
                                                        "sire": "509",
                                                        "children": [
                                                            {
                                                                "name": "Török Giovannik",
                                                                "id": "511",
                                                                "sire": "510"
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "name": "Marianna Giovanni",
                                                "id": "512",
                                                "sire": "464",
                                                "children": [
                                                    {
                                                        "name": "Lorenzo Giovanni",
                                                        "id": "513",
                                                        "sire": "512"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    };
	
	//end
    //init Spacetree
    //Create a new ST instance
    var st = new $jit.ST({
        //id of viz container element
        injectInto: 'infovis',

        //SET THE TREE TO VERTICAL
        orientation:"top",

        //set duration for the animation
        duration: 800,
        //set animation transition type
        transition: $jit.Trans.Quart.easeInOut,
        //set distance between node and its children
        levelDistance: 50,
        //enable panning
        Navigation: {
          enable:true,
          panning:true
        },
        //set node and edge styles
        //set overridable=true for styling individual
        //nodes or edges
        Node: {
            height: 30,
            width: 60,
            type: 'rectangle',
            color: '#aaa',
            overridable: true
        },
        
        Edge: {
            type: 'bezier',
            overridable: true
        },
        
        onBeforeCompute: function(node){
            Log.write("loading " + node.name);
        },
        
        onAfterCompute: function(){
            Log.write("done");
        },
        
        //This method is called on DOM label creation.
        //Use this method to add event handlers and styles to
        //your node.
        onCreateLabel: function(label, node){
            label.id = node.id;            
            label.innerHTML = node.name;
            label.onclick = function(){
            	if(normal.checked) {
            	  st.onClick(node.id);
            	} else {
                st.setRoot(node.id, 'animate');
            	}
            };
            //set label styles
            var style = label.style;
            style.width = 60 + 'px';
            style.height = 17 + 'px';            
            style.cursor = 'pointer';
            style.color = '#333';
            style.fontSize = '0.8em';
            style.textAlign= 'center';
            style.paddingTop = '3px';
        },
        
        //This method is called right before plotting
        //a node. It's useful for changing an individual node
        //style properties before plotting it.
        //The data properties prefixed with a dollar
        //sign will override the global node style properties.
        onBeforePlotNode: function(node){
            //add some color to the nodes in the path between the
            //root node and the selected node.
            if (node.selected) {
                node.data.$color = "#ff7";
            }
            else {
                delete node.data.$color;
                //if the node belongs to the last plotted level
                if(!node.anySubnode("exist")) {
                    //count children number
                    var count = 0;
                    node.eachSubnode(function(n) { count++; });
                    //assign a node color based on
                    //how many children it has
                    node.data.$color = ['#aaa', '#baa', '#caa', '#daa', '#eaa', '#faa'][count];                    
                }
            }
        },
        
        //This method is called right before plotting
        //an edge. It's useful for changing an individual edge
        //style properties before plotting it.
        //Edge data proprties prefixed with a dollar sign will
        //override the Edge global style properties.
        onBeforePlotLine: function(adj){
            if (adj.nodeFrom.selected && adj.nodeTo.selected) {
                adj.data.$color = "#eed";
                adj.data.$lineWidth = 3;
            }
            else {
                delete adj.data.$color;
                delete adj.data.$lineWidth;
            }
        }
    });
    //load json data
    st.loadJSON(json);
    //compute node positions and layout
    st.compute();
    //optional: make a translation of the tree
    st.geom.translate(new $jit.Complex(-200, 0), "current");
    //emulate a click on the root node.
    st.onClick(st.root);
    //end
    //Add event handlers to switch spacetree orientation.
    var top = $jit.id('r-top'), 
        left = $jit.id('r-left'), 
        bottom = $jit.id('r-bottom'), 
        right = $jit.id('r-right'),
        normal = $jit.id('s-normal');
        
    
    function changeHandler() {
        if(this.checked) {
            top.disabled = bottom.disabled = right.disabled = left.disabled = true;
            st.switchPosition(this.value, "animate", {
                onComplete: function(){
                    top.disabled = bottom.disabled = right.disabled = left.disabled = false;
                }
            });
        }
    };
    
    top.onchange = left.onchange = bottom.onchange = right.onchange = changeHandler;
    //end

}
