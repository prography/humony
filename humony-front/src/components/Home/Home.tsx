import React, { Component } from 'react';
import styled from 'styled-components';
import './Home.scss';
import * as api from '../../lib/api';
import swal from 'sweetalert';
//import console = require('console');


interface Props {
    
};

interface State {
    formData: any
};

class Home extends Component<Props, State> {
    state = {
        formData: ''
    };

    handleChange = (e: any) => {
        const files: any = Array.from(e.target.files);

        const formData = new FormData();

        files.forEach((file: any, i: any) => {
            formData.append('before', file); 
        });

        if (files.length) {
            this.setState({
                formData: formData
            });
        }
        
    }

    handleUpload = async () => {
        if (!this.state.formData) {
            swal('파일을 선택해 주세요');
            return false;
        }

        try {
            await api.sendImage(this.state.formData);

            swal('업로드 성공', '이미지 업로드에 성공했습니다.', 'success');
        } catch {
            swal('업로드 실패','이미지 업로드에 실패했습니다.', 'error');
        }
    }

    render () {
        const SendBtn = styled.button`
            margin-top: 10px;
            padding: 10px;
            background: #3498db;
            color: #fff;
            border-radius: 3px;
        `;

        return (
            <section id="home">
                <div className="home-wrap">
                    <div className="uploadBox">
                        <h2>파일 업로드</h2>
                        <form>
                            <div className="filebox">
                                <label htmlFor="ex_file">
                                    파일을 선택해 주세요
                                </label>
                                <input type="file" onChange={this.handleChange} id="ex_file" />
                            </div>
                        </form>
                        <SendBtn type="button" onClick={this.handleUpload}>전송</SendBtn>
                    </div>
                    <div className="titleInfo">
                        <h3><span className="title-concept">사진을 쉽고 빠르게 자르자!</span> <br/>윤대영쌤의 딥러닝과 함께하는<br/>재미있는 누끼따기</h3>
                        <button className="startBtn"><span>START</span> 지금 바로 시작하기</button>  
                    </div>
                </div>
            </section>
        );
    }
}

export default Home;