import React, { Component } from 'react';
import styled from 'styled-components';
import './Home.scss';
import * as api from '../../lib/api';
import swal from 'sweetalert';
import { IoIosCloudUpload as UploadIcon } from 'react-icons/io';


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
            swal('파일을 선택해 주세요', '', 'warning');
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
            <div id="home">
                <section className="main-banner">
                    <div className="main-content">
                        <div className="main-container">
                            <div className="main-title-info">
                                <h2>사진을 10초만에 자르기<br/>픽시와 함께라면 가능합니다.</h2>
                                <p>지금 바로 시작해보세요!</p>
                            </div>
                            <div className="upload-box">
                                <div className="ub-bg">
                                    <label htmlFor="imageInput">
                                        <figure>
                                            <UploadIcon className="upload-icon" />
                                        </figure>
                                        <span>이미지 파일을 선택해주세요 <br/><span className="ext">JPG, JPGEG, PNG</span></span>
                                    </label>
                                    <input type="file" id="imageInput" onChange={this.handleChange} />
                                    <button type="button" onClick={this.handleUpload}>전송하기</button>
                                </div>  
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        );
    }
}

export default Home;