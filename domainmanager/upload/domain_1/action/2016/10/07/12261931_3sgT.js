document.write("<!DOCTYPE html>\r\n<html>\r\n<head>\n<!-- Adform API Script -->\n<script type=\"text/javascript\">\n    document.write('<script src=\"'+ (window.API_URL || 'https://s1.adform.net/banners/scripts/rmb/Adform.DHTML.js?bv='+ Math.random()) +'\"><\\/script>');\n</script>\r\n    <meta charset=\"utf-8\" />\r\n    <title>Hyundai IONIQ</title>\r\n    <style>\r\n    \r\n        html {-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing: border-box;}\r\n        *, *::before, *::after {-webkit-box-sizing: inherit; -moz-box-sizing: inherit; box-sizing: inherit;}\r\n        \r\n        body {margin: 0px; background: rgb(247, 252, 255);}\r\n        #main {width: 300px; height: 600px; position: relative;}\r\n        \r\n        a {position: absolute; z-index: 10;}\r\n        a#x {right: 0px; top: 0px; width: 17px; height: 17px;}\r\n        a#clicktag {left: 0px; top: 0px; width: 100%; height: 100%;}\r\n        img {display: block;}\r\n        \r\n        #h {position: absolute; left: 0px; top: 0px; width: 300px; height: 170px; background: url(h.png) no-repeat;}\r\n        #f {position: absolute; left: 0px; bottom: 0px; width: 300px; height: 110px; background: url(f.png) no-repeat;}\r\n        \r\n        .s {position: absolute; left: 0px; top: 170px; width: 300px; height: 320px; overflow: hidden;}\r\n        \r\n        #s1 {background: url(1.jpg) 0px 0px no-repeat;}\r\n        \r\n        #s2 {opacity: 0; background: rgb(247, 252, 255);}\r\n        #s2 img {position: absolute; left: 300px;}\r\n        #i2_1 {top: 0px;}\r\n        #i2_2 {top: 105px;}\r\n        #i2_3 {top: 210px;}\r\n        \r\n        #s3 {opacity: 0; background: url(3.jpg) 0px bottom no-repeat;}\r\n        #i3_t {opacity: 0; position: absolute; left: 78px; top: 18px;}\r\n        \r\n        #s4 {opacity: 0; background: url(4.jpg) 0px bottom no-repeat;}\r\n        #s4 img {position: absolute;}\r\n        #i4_b {opacity: 0; left: 50px; top: 100px;}\r\n        #i4_p {left: 300px; top: 100px;}\r\n        \r\n    </style>\r\n    <script src=\"//cdn.jsdelivr.net/velocity/1.2.3/velocity.min.js\"></script>\r\n    <script src=\"//cdn.jsdelivr.net/velocity/1.2.3/velocity.ui.min.js\"></script>\r\n    <script>\r\n        \r\n        function x() {var e = document.getElementById(\"main\"); e.parentNode.removeChild(e);}\r\n        \r\n        window.onload = function() {\r\n            \r\n            var loop = 0;\r\n            \r\n            function ge(id) {return document.getElementById(id);}\r\n            \r\n            var sequence = [\r\n                {e: ge(\"s1\"),   p: {backgroundPositionX: -67}, o: {duration: 1500, easing: \"ease-in-out\", delay: 500}},\r\n                {e: ge(\"s2\"),   p: {opacity: 1}, o: {duration: 250, easing: \"ease-in-out\"}},\r\n                {e: ge(\"i2_1\"), p: {left: 40}, o: {duration: 400, easing: \"ease-in-out\"}},\r\n                {e: ge(\"i2_2\"), p: {left: 40}, o: {duration: 400, easing: \"ease-in-out\"}},\r\n                {e: ge(\"i2_3\"), p: {left: 40}, o: {duration: 400, easing: \"ease-in-out\"}},\r\n                {e: ge(\"s3\"),   p: {opacity: 1}, o: {duration: 250, easing: \"ease-in-out\", delay: 500}},\r\n                {e: ge(\"i3_t\"), p: {opacity: 1, scale: [1, 0.1]}, o: {duration: 800, easing: \"spring\"}},\r\n                {e: ge(\"s4\"),   p: {opacity: 1}, o: {duration: 250, easing: \"ease-in-out\", delay: 1000}},\r\n                {e: ge(\"i4_b\"), p: {opacity: 1, scale: [1, 0.1]}, o: {duration: 800, easing: \"spring\"}},\r\n                {e: ge(\"i4_p\"), p: {left: 226, top: 124}, o: {duration: 300, easing: \"ease-out\"}},\r\n                {e: ge(\"i4_p\"), p: {scale: [0.8, 1]}, o: {duration: 100, easing: \"swing\"}},\r\n                {e: ge(\"i4_p\"), p: {scale: [1, 0.8]}, o: {duration: 100, easing: \"swing\"}},\r\n                {e: ge(\"i4_p\"), p: {left: 246, top: 320}, o: {duration: 300, easing: \"ease-in\", complete: function(e) {\r\n                    if(loop < 3)\r\n                    //if(1)\r\n                    {\r\n                        ge(\"s1\").style.backgroundPosition = \"0px 0px\";\r\n                        ge(\"s2\").style.opacity = 0;\r\n                        ge(\"i2_1\").style.left = \"300px\";\r\n                        ge(\"i2_2\").style.left = \"300px\";\r\n                        ge(\"i2_3\").style.left = \"300px\";\r\n                        ge(\"s3\").style.opacity = 0;\r\n                        ge(\"i3_t\").style.opacity = 0;\r\n                        ge(\"i4_p\").style.left = \"300px\";\r\n                        ge(\"i4_p\").style.top = \"100px\";\r\n                        \r\n                        Velocity(ge(\"s4\"), {opacity: 0}, {duration: 250, delay: 3000, complete: function(e) {\r\n                            ge(\"i4_b\").style.opacity = 0;\r\n                            Velocity.RunSequence(sequence);\r\n                        }});\r\n                        \r\n                        loop++;\r\n                    }\r\n                }}}\r\n            ];\r\n\r\n            Velocity.RunSequence(sequence);\r\n            \r\n        }\r\n        \r\n        var getUriParams = function() {\r\n            var query_string = {}\r\n            var query = window.location.search.substring(1);\r\n            var parmsArray = query.split('&');\r\n            if(parmsArray.length <= 0) return query_string;\r\n            for(var i = 0; i < parmsArray.length; i++) {\r\n                var pair = parmsArray[i].split('=');\r\n                var val = decodeURIComponent(pair[1]);\r\n                if (val != '' && pair[0] != '') query_string[pair[0]] = val;\r\n            }\r\n            return query_string;\r\n        }();\r\n        \r\n    </script>\r\n<!--Adform Global Clicktag START-->\n<script type=\"text/javascript\">\n    function adfOpenGlobalClickTAG() {\n        var adfClickTAGName = 'clickTAG',\n            adfClickTAGUrl = 'http://www.hyundai.at/Showroom/Cars/IONIQ-Hybrid.aspx?utm_source=Adverserve_RTB_Reach&utm_medium=HalfpageAd&utm_campaign=Hyundai_IONIQ_PreLaunch';\n\n        window.open(dhtml.getVar(adfClickTAGName, adfClickTAGUrl), dhtml.getVar('landingPageTarget', '_blank'));\n    }\n    if(window.addEventListener) {\n        window.addEventListener('click', function(e) {\n            if(e.button !== 0) return;\n            e.stopPropagation();\n            e.preventDefault();\n            adfOpenGlobalClickTAG();\n        }, true);\n    } else {\n        document.attachEvent('onclick', function() {\n            adfOpenGlobalClickTAG();\n        });\n    }\n</script>\n<style>\n    html {\n        cursor: pointer;\n    }\n</style>\n<!--Adform Global Clicktag END-->\n\n</head>\r\n<body>\r\n\r\n\r\n\r\n<div id=\"main\">\r\n    <a id=\"clicktag\" href=\"#clicktag\" target=\"_blank\"></a>\r\n    <script>document.getElementById('clicktag').setAttribute('href', getUriParams.clicktag);</script>\r\n    <!--<a id=\"x\" href=\"#\" onclick=\"x(); return false;\"></a>-->\r\n    <div id=\"h\"></div>\r\n    <div id=\"s1\" class=\"s\"></div>\r\n    <div id=\"s2\" class=\"s\">\r\n        <img id=\"i2_1\" src=\"2_1.png\" />\r\n        <img id=\"i2_2\" src=\"2_2.png\" />\r\n        <img id=\"i2_3\" src=\"2_3.png\" />\r\n    </div>\r\n    <div id=\"s3\" class=\"s\">\r\n        <img id=\"i3_t\" src=\"3_t.png\" />\r\n    </div>\r\n    <div id=\"s4\" class=\"s\">\r\n        <img id=\"i4_b\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAAAyCAYAAAD/eF+lAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MkI5NjA2MDU1NEMxMTFFNkE0MjY4RTUyOTFBRjgyRjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MkI5NjA2MDY1NEMxMTFFNkE0MjY4RTUyOTFBRjgyRjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoyQjk2MDYwMzU0QzExMUU2QTQyNjhFNTI5MUFGODJGMiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDoyQjk2MDYwNDU0QzExMUU2QTQyNjhFNTI5MUFGODJGMiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PhP8ljMAAAfhSURBVHja7J0LbBRF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\" />\r\n        <img id=\"i4_p\" src=\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAXCAYAAADtNKTnAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoV2luZG93cykiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MEI4RDdCMzI1NEMxMTFFNkJERTlDN0ZBQThFRUI1NjgiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MEI4RDdCMzM1NEMxMTFFNkJERTlDN0ZBQThFRUI1NjgiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowQjhEN0IzMDU0QzExMUU2QkRFOUM3RkFBOEVFQjU2OCIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowQjhEN0IzMTU0QzExMUU2QkRFOUM3RkFBOEVFQjU2OCIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Pu4L0YkAAAKlSURBVHjanFQ9aBNhGH7z3cUUUsRGoWkGk0gGVxfpYLSDOnVoB/tjoWCdnHQW3Ct0totQO4kIxbWCSwst6JRFXKIttUrbC6SS5PLX+3yez0s4jysVX3jyvffd+z55fy+mtZagxCA4ngAJ4LkOG0QJbXqAKODxzPSMvjc1xYtHvAvaRCFMci6RSOh2u61brZamzruzSOxwYHB2KpXKJc/zBPqh/IOo01IkCVXg5L9IKPF4nEcSuIVaX/1T72ixT4uEJGNjY4OI6EOn25Xtra0JEO3gtQWUYHNyJkkXjkpZsrKyIul0WorFm+/cpiupoSHZ3NycBeE2TL+T7NSaUDqdttTrdRkYGJBs7rK8AuHGxoaMj4+/zufzjGoOZErhJw2MAIO4ZDVPIKawx8fHfDCEFacibqNh9EKhIMvLL2R+fn4Vjw8Yyc/h4eEfON8CVzi0vZrcKBYlmUwawtHRUbmAVCgkPzg8ktVVcshLP3qt19bWdCqV0rlcTu/v7+tGo6GbzWb/REQGlMXFRb3+fl37K2Fy/7i0tGQMS6WSnpycNCS1Wk2jHgau62oU2pAgKh0UkrD554E3wG3HcWzWwLZtUZYlKJhYOAmlVP8Mzgx1Ltcv6LNAAztjOuG3qD+5RFDvPYcntgV8ymQyHuej56AD7Y4iCpO4wARQRS1MyCYY35Ep9on9CJnG7u4uzQ5UYLgYTTmbzXpBYx1Kq/eOf7Sw8JB+08GJ7QB3gCan1LLtvz5aUfVwnCNzxIIFQoj0/ALkq9WqYhoMO8aOcPP87rB7eC8Y0i6ur4V3h5fXmdbe3l7vc2A6Fdwp3t+fm6N6F/hshxcP/8yWX9xB0TA30sYSmmg4MzFloiLJ13KZLt/g48UivvYkfgqM+HWKEsvv7DP4O78FGAAvWhnXLrShHQAAAABJRU5ErkJggg==\" />\r\n    </div>\r\n    <div id=\"f\"></div>\r\n</div>\r\n\r\n\r\n\r\n</body>\r\n</html>");