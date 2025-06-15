
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trump Timeline", layout="wide")
st.title("Trump vs. Harvard Timeline")

html_code = """
<!DOCTYPE html>
<html>
  <head>
    <!-- TimelineJS -->
    <link rel="stylesheet" href="https://cdn.knightlab.com/libs/timeline3/latest/css/timeline.css">
    <script src="https://cdn.knightlab.com/libs/timeline3/latest/js/timeline.js"></script>

    <!-- Load Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Noto+Sans+KR&display=swap" rel="stylesheet">

    <style>
      html, body {
        margin: 0;
        padding: 0;
        height: 100%;
      }

      /* Title / Headline */
      .tl-headline, .tl-title, .tl-slide .tl-text h2 {
        font-family: 'Do Hyeon', sans-serif !important;
        # letter-spacing: 0.03em !important;
        line-height: 1.5 !important;
        font-weight: normal;
      }

      /* Body Text */
      .tl-text-content, .tl-text-content p, .tl-text-content li {
        font-family: 'Noto Sans KR', sans-serif !important;
        line-height: 1.5 !important;
        font-weight: 400;
      }
       /* Media caption and credit */
  .tl-media .tl-caption,
  .tl-media .tl-credit {
    font-family: 'Noto Sans KR', sans-serif !important;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.5 !important;
  }

      #timeline-embed {
        width: 100%;
        height: 100vh;
      }
    </style>
  </head>
  <body>
    <div id="timeline-embed"></div>
    <script>
      var additionalOptions = {
        initial_zoom: 5
      };
      window.timeline = new TL.Timeline(
        'timeline-embed',
        'https://raw.githubusercontent.com/hana1101/trump_timeline/main/timeline.json',
        additionalOptions
      );
    </script>
  </body>
</html>
"""

components.html(html_code, height=800)
