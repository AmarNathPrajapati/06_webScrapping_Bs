from bs4 import BeautifulSoup

html_content = """
<li class="b_algo b_ccontain" data-id="">
    <div class="tpcn"><a class="tilk" target="_blank"
            href="https://www.bing.com/ck/a?!&amp;&amp;p=214aed016ae71775JmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NTI5Ng&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1aHR0cHM6Ly9ibG9nLmdvb2dsZS9hdXRob3JzL3N1bmRhci1waWNoYWkv&amp;ntb=1"
            h="ID=SERP,5296.1">
            <div class="tpic">
                <div class="wr_fav" data-priority="2">
                    <div class="cico siteicon" style="width:32px;height:32px;">
                        <div class="rms_iac" style="height:32px;line-height:32px;width:32px;" data-height="32"
                            data-width="32" data-alt="Global web icon" data-class="rms_img"
                            data-src="https://th.bing.com/th?id=ODLS.53284b05-912c-4473-8b4f-48963e350ba8&amp;w=32&amp;h=32&amp;qlt=92&amp;pcl=fffffa&amp;o=6&amp;pid=1.2">
                        </div>
                    </div>
                </div>
            </div>
            <div class="tptxt">
                <div class="tptt">The Keyword</div>
                <div class="tpmeta">
                    <div class="b_attribution" u="2|5115|4957612401965543|DHNTfmMQ9r_OdlFZYHauzQxp1rTJUpBi"
                        tabindex="0"><cite>https://blog.google/authors/sundar-pichai</cite><span class="c_tlbxTrg"><span
                                class="c_tlbxH" H="BASE:CACHEDPAGEDEFAULT" K="SERP,5297.1"></span><span class="c_tlbxH"
                                H="BASE:GENERATIVECAPTIONSHINTSIGNAL" K="SERP,5302.1"></span></span></div>
                </div>
            </div>
        </a></div>
    <h2><a target="_blank"
            href="https://www.bing.com/ck/a?!&amp;&amp;p=214aed016ae71775JmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NTI5Ng&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1aHR0cHM6Ly9ibG9nLmdvb2dsZS9hdXRob3JzL3N1bmRhci1waWNoYWkv&amp;ntb=1"
            h="ID=SERP,5296.2">Sundar Pichai | Google Blog - The Keyword</a></h2>
    <div class="b_caption" role="contentinfo">
        <p class="b_lineclamp2 b_algoSlug"><span class="algoSlug_icon" data-priority="2">WEB</span>Learn about Sundar
            Pichai, the CEO of Google and Alphabet, and his vision for the company's products and services. Read his
            latest articles on AI, AI-powered products, and …</p>
    </div>
    <div class="pageRecoPlaceholder" data-tag="RelatedPageRecommendations.RecommendationsClickback"></div>
    <div class="scs_child_rpr rpr_light">
        <div class="pageRecoContainer " data-fbhlsel=".pageRecoContainer">
            <div class="recommendationsTableTitle">
                <h2 class="">Explore further</h2>
            </div>
            <div class="pagereco_TCntr">
                <div class="pagereco_TRow  ">
                    <div class="pagereco_TTitle"><a target="_blank"
                            href="https://www.bing.com/ck/a?!&amp;&amp;p=74e7a32a0568f9faJmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NjAyMg&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1aHR0cHM6Ly93aWtpYmlvLmluL3N1bmRhci1waWNoYWkv&amp;ntb=1"
                            h="ID=SERP,6022.1">
                            <div class="b_fpl_cntr">
                                <div class="b_fpl_icon" data-priority="2">
                                    <div class="cico siteicon" style="width:16px;height:16px;">
                                        <div class="rms_iac" style="height:16px;line-height:16px;width:16px;"
                                            data-height="16" data-width="16" data-alt="Global web icon" data-role="img"
                                            data-class="rms_img"
                                            data-src="https://th.bing.com/th?id=ODLS.cee71abf-f4fe-472b-8a3e-2762a45a12dd&amp;w=16&amp;h=16&amp;o=6&amp;pid=1.2">
                                        </div>
                                    </div>
                                </div>
                                <div class="b_fpl_attr">
                                    <div class="b_title">Sundar Pichai Wiki, <strong>Age, Wife, Children, Family,
                                            Biography &amp;</strong> …</div>
                                </div>
                            </div>
                        </a></div>
                    <div class="pagereco_TDomain"><a target="_blank"
                            href="https://www.bing.com/ck/a?!&amp;&amp;p=74e7a32a0568f9faJmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NjAyMg&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1aHR0cHM6Ly93aWtpYmlvLmluL3N1bmRhci1waWNoYWkv&amp;ntb=1"
                            h="ID=SERP,6022.2">
                            <div class="b_attr"><cite>wikibio.in</cite></div>
                        </a></div>
                </div>
                <div class="pagereco_TRow  ">
                    <div class="pagereco_TTitle"><a target="_blank"
                            href="https://www.bing.com/ck/a?!&amp;&amp;p=a38f53329e240089JmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NjAyMw&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1aHR0cHM6Ly93d3cuYmJjLmNvbS9uZXdzL3RlY2hub2xvZ3ktNTc3NjMzODI&amp;ntb=1"
                            h="ID=SERP,6023.1">
                            <div class="b_fpl_cntr">
                                <div class="b_fpl_icon" data-priority="2">
                                    <div class="cico siteicon" style="width:16px;height:16px;">
                                        <div class="rms_iac" style="height:16px;line-height:16px;width:16px;"
                                            data-height="16" data-width="16" data-alt="Global web icon" data-role="img"
                                            data-class="rms_img"
                                            data-src="https://th.bing.com/th?id=ODLS.117fffdc-32dc-4d03-9400-59cb5a88df5c&amp;w=16&amp;h=16&amp;o=6&amp;pid=1.2">
                                        </div>
                                    </div>
                                </div>
                                <div class="b_fpl_attr">
                                    <div class="b_title">Google boss <strong>Sundar Pichai warns of threats to
                                            internet</strong> …</div>
                                </div>
                            </div>
                        </a></div>
                    <div class="pagereco_TDomain"><a target="_blank"
                            href="https://www.bing.com/ck/a?!&amp;&amp;p=a38f53329e240089JmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NjAyMw&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1aHR0cHM6Ly93d3cuYmJjLmNvbS9uZXdzL3RlY2hub2xvZ3ktNTc3NjMzODI&amp;ntb=1"
                            h="ID=SERP,6023.2">
                            <div class="b_attr"><cite>bbc.com</cite></div>
                        </a></div>
                </div>
            </div>
            <div class="recommendationsTableFeedback">
                <div class="fbans">
                    <div class="b_footnote"><a id="fdbkans_1" class="hlig" target="_blank"
                            data-fbhlsel=".pageRecoContainer" role="button"
                            href="https://www.bing.com/ck/a?!&amp;&amp;p=4244c5f6269742fcJmltdHM9MTcxMDI4ODAwMCZpZ3VpZD0wZDVlNDEzMy0zNzliLTY3ZjAtMzM3OC01MmNkMzYwMDY2ZWEmaW5zaWQ9NjMwMQ&amp;ptn=3&amp;ver=2&amp;hsh=3&amp;fclid=0d5e4133-379b-67f0-3378-52cd360066ea&amp;psq=google+ceo&amp;u=a1amF2YXNjcmlwdDp2b2lkKDAp&amp;ntb=1"
                            h="ID=SERP,6301.1">Recommended to you based on what's popular • Feedback</a></div>
                </div>
            </div>
        </div>
    </div>
</li>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Find all <li> tags with class "b_algo b_ccontain"
results = soup.find_all("li", class_="b_algo b_ccontain")

for result in results:
    # Find the text of the anchor tag inside h2
    h2_text = result.find("h2").find("a").text.strip()

    # Find the text of p tag with class "b_lineclamp2 b_algoSlug"
    p_text = result.find("p", class_="b_lineclamp2 b_algoSlug").text.strip()

    print(h2_text)
    print(p_text)

