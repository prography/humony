import React from 'react';
import './Intro.scss';
import Macbook from '../../assets/images/macbook.png';
import Intro2 from '../../assets/images/intro2.png';
import Clock from '../../assets/images/clock.png';

const Intro: React.FC = () => {
    return (
        <React.Fragment>
            <section id="intro">
                <div className="intro-wrap">
                    <div className="main-title">
                        <h2><span className="color-main">PICXY</span> 서비스 소개</h2>
                        <p>포토샵, 일러스트로 자르기 힘든 사진을 쉽게 자를 수 있도록<br/>단 한번의 업로드로 사진을 분할하며, 원하는 부분만 클릭해서<br/>쉽게 다운로드 할 수 있습니다.<br/><br/></p>
                        <button className="startBtn"><span>START</span> 지금 바로 시작하기</button>  
                    </div>
                    <div className="image-wrap">
                        <img src={Macbook} alt="macbook" width="650" />
                    </div>
                </div>
            </section>
            <section id="intro2">
                <div className="intro-wrap">
                    <div className="main-title">
                        <h2><span className="color-main">빠르게</span> 분할하기</h2>
                        <p>어려운 사진분할 작업을 픽시로 10초만에 분할할 수 있어요<br/>업로드 한번만 하면 픽시가 사진을 분할해줍니다.</p>
                    </div>
                    <div className="image-wrap">
                        <img src={Intro2} alt="intro2"/>
                        <img src={Clock} alt="clock"/>
                    </div>
                </div>
            </section>
            <section id="intro3">
                
            </section>
        </React.Fragment>
    );
};

export default Intro;