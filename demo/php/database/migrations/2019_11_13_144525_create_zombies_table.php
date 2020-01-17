<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateZombiesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('zombies', function (Blueprint $table) {
            $table->increments('id');
            $table->string('webUser',255)->nullable(false)->comment('web端登录的账号');
            $table->string('cwxid',255)->nullable(false)->comment('登陆微信号');
            $table->string('wxid',255)->nullable(false);
            $table->string('nick',255)->nullable()->comment('昵称');
            $table->string('username',255)->nullable()->comment('微信账号 用户设置的');
            $table->string('asName',255)->nullable()->comment('备注名');
            $table->string('headPic',255)->nullable()->comment('头像');
            $table->tinyInteger('sex')->default(1)->comment('性别');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('zombies');
    }
}
