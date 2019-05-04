import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './Header.scss';

interface Props {
    scrollTop: number
}

interface State {
    mobileOpen: boolean
}


class Header extends Component<Props, State> {
    state = {
        mobileOpen: false
    }

    handleClick = () => {
        this.setState({
            mobileOpen: !this.state.mobileOpen
        });
    }

    render () {
        return (
            <header className={ this.props.scrollTop >= 100 ? 'header-fix' : ''}>
                <nav>
                    <div className="header-container">
                        <div className="logo">
                            <Link to="/">PICXY</Link>
                        </div>
                        <ul className={`gnb_list ${this.state.mobileOpen ? 'is_open' : ''}`}>
                            <li><Link to="/">홈</Link></li>
                            <li><Link to="/intro">서비스 소개</Link></li>
                            <li><Link to="#">픽시 플러스</Link></li>
                        </ul>
                        <div className={`mobile-menu ${this.state.mobileOpen ? 'is_open' : ''}`} onClick={this.handleClick}>
                            <div className="bar"></div>
                            <div className="bar"></div>
                            <div className="bar"></div>
                        </div>
                    </div>
                </nav>
            </header>
        );
    }
}

export default Header;